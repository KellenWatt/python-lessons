from restaurant.pos import POS
from restaurant.finance import Finance
from restaurant.inventory import Inventory

import random
import string
import sys
import inspect
import traceback

MAX_NAME_LENGTH = 20
MAX_ITEM_COUNT = 1000
MAX_DICT_SIZE = 20
BALANCE_LIMIT = 10000
MAX_ORDER_SIZE = 50

def red(text: str) -> str:
    return "\033[91m" + text + "\033[0m"

def green(text: str) -> str:
    return "\033[32m" + text + "\033[0m"

def blue(text: str) -> str:
    return "\033[36m" + text + "\033[0m"

def rand_count(max = MAX_ITEM_COUNT) -> int:
    return random.randint(1, max)

def make_random_name() -> str:
    size = random.randint(1, MAX_NAME_LENGTH+1)
    return "".join(random.choice(string.ascii_letters) for _ in range(size))

def make_random_dict() -> dict:
    return {make_random_name(): random.randint(1, MAX_ITEM_COUNT) for _ in range(MAX_DICT_SIZE)}

def make_bad_key(dict: dict) -> str:
    bad_key = make_random_name()
    while bad_key in dict:
        bad_key = make_random_name()
    return bad_key

def random_item(inv: Inventory) -> str:
    return random.choice(list(inv.full_inventory().keys()))

def random_balance(upper: float = BALANCE_LIMIT) -> float:
    return random.random() * upper + 0.01

def close_enough(given, expected, delta = 0.001):
    return abs(given - expected) < delta

class Dish:
    pass

def make_menu(inventory: Inventory | dict) -> dict:
    menu = {}
    for _ in range(random.randint(1, 10)):
        d = Dish()
        d.price = random_balance()
        d.ingredients = {}
        for _ in range(random.randint(1, 5)):
            if type(inventory) == type({}):
                item = random.choice(list(inventory.keys()))
            else:
                item = random_item(inventory)
            d.ingredients[item] = rand_count(MAX_ITEM_COUNT / 100)
        menu[make_random_name()] = d
    return menu

def make_catalogue(inventory: dict, **extras) -> dict:
    # Add existing inventory to catalogue
    cat = {item: random_balance(BALANCE_LIMIT / 100) for item in inventory}
    # Add random extras to catalogue
    for _ in range(5):
        cat[make_random_name()] = random_balance(BALANCE_LIMIT / 100)
    # Add any specific values for testing purposes
    for item, price in extras.items():
        cat[item] = price
    return cat

def make_order(catalogue: dict, size:int = 0) -> dict:
    if size <= 0:
        size = random.randint(1, 5)
    return {random.choice(list(catalogue.keys())): random.randint(1, MAX_ORDER_SIZE) for _ in range(size)}


def test_Inventory_is_created():
    d = make_random_dict()
    inv = Inventory(d.copy())
    assert inv is not None

def test_Inventory_is_created_for_empty_dict():
    inv = Inventory({})
    assert inv is not None

def test_Inventory_full_inventory_returns_inventory():
    expected = make_random_dict()
    inv = Inventory(expected.copy())
    assert expected == inv.full_inventory(), "The passed-in inventory was not stored correctly"

def test_Inventory_current_inventory_returns_in_stock_inventory():
    d = make_random_dict()
    d["a"] = 0
    expected = {k:v for k,v in d.items() if v > 0}
    inv = Inventory(d)
    assert expected == inv.current_inventory()

def test_Inventory_current_is_different_from_full_inventory_when_item_out_of_stock():
    d = make_random_dict()
    d["a"] = 0
    inv = Inventory(d)
    assert inv.full_inventory() != inv.current_inventory()

def test_Inventory_amount_returns_counts():
    d = make_random_dict()
    inv = Inventory(d.copy())
    assert all(inv.amount(item) == d[item] for item in d), "Not all counts were the same as original"

def test_Inventory_amount_returns_None_on_invalid_item():
    d = make_random_dict()
    inv = Inventory(d.copy())
    bad_key = make_bad_key(d)
    assert inv.amount(bad_key) == None

def test_Inventory_multiple_inventories_are_independent():
    d, e = make_random_dict(), make_random_dict()
    while d == e:
        e = make_random_dict()
    inv1 = Inventory(d.copy())
    inv2 = Inventory(e.copy())
    assert inv1.full_inventory() != inv2.full_inventory()

def test_Inventory_use_subtracts_amount_given():
    inv = Inventory(make_random_dict())
    item = random_item(inv)
    current_count = inv.full_inventory()[item]
    used = rand_count(current_count)
    inv.use(item, used)
    assert inv.amount(item) == current_count - used

def test_Inventory_use_can_use_exact_amount():
    d = make_random_dict()
    d["a"] = 1 # insert specific test case
    inv = Inventory(d)
    for k in inv.full_inventory():
        inv.use(k, inv.amount(k))
    assert all(c == 0 for _,c in inv.full_inventory().items()), "An item did not allow exact stock to be used"

def test_Inventory_use_does_not_subtract_more_than_amount():
    basic = {"a": 0}
    inv = Inventory(basic.copy())
    inv.use("a", 1)
    assert inv.full_inventory() == basic, "Out-of-stock item used"

    inv = Inventory(make_random_dict())
    item = random_item(inv)
    current_count = inv.full_inventory()[item]
    inv.use(item, current_count + 1)
    assert inv.amount(item) == current_count, "More items used than in-stock"

def test_Inventory_use_does_nothing_for_nonexistent_items():
    d = make_random_dict()
    inv = Inventory(d.copy())
    bad_key = make_bad_key(d)
    inv.use(bad_key, 1)
    assert inv.full_inventory() == d

def test_Inventory_stock_adds_item_to_inventory():
    inv = Inventory(make_random_dict())
    item = random_item(inv)
    current_count = inv.amount(item)
    amount = rand_count()
    inv.stock(item, amount)
    assert inv.amount(item) == current_count + amount

def test_Inventory_stock_adds_nonexistent_item_to_inventory():
    inv = Inventory(make_random_dict())
    new_item = make_bad_key(inv.full_inventory())
    amount = rand_count()
    inv.stock(new_item, amount)
    assert inv.amount(new_item) == amount

def test_Inventory_is_stocked_is_true_for_all_full_inventory():
    inv = Inventory(make_random_dict())
    for k, v in inv.full_inventory().items():
        if v > 0:
            assert inv.is_stocked(k)

def test_Inventory_is_stocked_is_false_for_items_with_no_stock():
    inv = Inventory({"a": 0})
    assert not inv.is_stocked("a")

def test_Inventory_is_stocked_is_false_for_nonexistent_items():
    inv = Inventory(make_random_dict())
    bad_key = make_bad_key(inv.full_inventory())
    assert not inv.is_stocked(bad_key)

def test_Inventory_has_enough_is_true_when_amount_is_less():
    inv = Inventory(make_random_dict())
    assert all(inv.has_enough(i, rand_count(a-1)) for i, a in inv.full_inventory().items() if a > 1)

def test_Inventory_has_enough_is_true_when_amount_is_equal():
    inv = Inventory(make_random_dict())
    assert all(inv.has_enough(i, a) for i, a in inv.full_inventory().items())

def test_Inventory_has_enough_is_false_when_amount_is_greater():
    inv = Inventory(make_random_dict())
    assert not any(inv.has_enough(i, a+1) for i, a in inv.full_inventory().items())

def test_Inventory_has_enough_is_false_when_item_is_nonexistent():
    inv = Inventory(make_random_dict())
    bad_key = make_bad_key(inv.full_inventory())
    assert not inv.has_enough(bad_key, 1)

def test_Inventory_in_history_works_for_full_inventory():
    inv = Inventory(make_random_dict())
    assert all(inv.in_history(k) for k in inv.full_inventory())

def test_Inventory_in_history_works_for_out_of_stock_items():
    d = make_random_dict()
    d["a"] = 0
    inv = Inventory(d)
    assert inv.in_history("a")

def test_Inventory_in_history_fails_for_nonexistent_item():
    inv = Inventory(make_random_dict())
    bad_key = make_bad_key(inv.full_inventory())
    assert not inv.in_history(bad_key)
    
def test_Finance_is_created():
    fin = Finance(0)
    assert fin is not None

def test_Finance_is_created_for_non_integers():
    fin = Finance(random_balance())
    assert fin is not None

def test_Finance_balance_lists_the_current_balance():
    b = random_balance()
    fin = Finance(b)
    assert fin.balance() == b

def test_Finance_debit_subtracts_money_from_the_balance():
    b = random_balance()
    fin = Finance(b)
    deb = random_balance(b/2)
    fin.debit(deb)
    assert close_enough(fin.balance(), b - deb)

def test_Finance_debit_does_not_change_when_greater_than_balance():
    b = random_balance()
    fin = Finance(b)
    fin.debit(b + 100)
    assert fin.balance() == b

def test_Finance_credit_adds_money_to_balance():
    b = random_balance()
    fin = Finance(b)
    cred = random_balance()
    fin.credit(cred)
    assert close_enough(fin.balance(), b + cred)

def test_Finance_credit_adds_money_to_zero_balance():
    fin = Finance(0)
    cred = random_balance()
    fin.credit(cred)
    assert fin.balance() == cred

def test_Finance_enough_funds_is_true_when_balance_sufficient():
    b = random_balance()
    fin = Finance(b)
    ask = b/2
    assert fin.enough_funds(ask)

def test_Finance_enough_funds_is_false_when_balance_insufficient():
    b = random_balance()
    fin = Finance(b)
    ask = b * 2
    assert not fin.enough_funds(ask)

    fin = Finance(0)
    assert not fin.enough_funds(0.01)

def test_Finance_transaction_log_is_empty_on_creation():
    fin = Finance(0)
    assert len(fin.transaction_log()) == 0

def test_Finance_transaction_log_reflects_successful_credit():
    fin = Finance(0)
    fin.credit(random_balance())
    assert len(fin.transaction_log()) == 1

def test_Finance_transaction_log_reflects_successful_debit():
    fin = Finance(100)
    fin.debit(100)
    assert len(fin.transaction_log()) == 1

def test_Finance_transaction_log_does_not_log_failed_debit():
    b = random_balance()
    fin = Finance(b)
    fin.debit(b+1)
    assert len(fin.transaction_log()) == 0

def test_Finance_transaction_log_shows_positive_number_for_credit():
    fin = Finance(0)
    cred = random_balance()
    fin.credit(cred)
    assert len(fin.transaction_log()) > 0
    assert fin.transaction_log()[0] == cred

def test_Finance_transaction_log_shows_negative_number_for_debit():
    b = random_balance()
    fin = Finance(b)
    deb = random_balance(b)
    fin.debit(deb)
    assert len(fin.transaction_log()) > 0
    assert fin.transaction_log()[0] == -deb

def test_Finance_transaction_log_shows_multiple_transactions():
    log = [random.choice([-1, 1]) * random_balance() for _ in range(100)]
    b = sum(abs(m) for m in log)
    fin = Finance(b) # to ensure there's enough money
    for entry in log:
        if entry < 0:
            fin.debit(-entry)
        else:
            fin.credit(entry)
    assert close_enough(sum(log) + b, fin.balance())
    assert len(fin.transaction_log()) == len(log)
    assert fin.transaction_log() == log


def test_POS_is_created():
    inv = make_random_dict()
    pos = POS(random_balance(), inv.copy(), make_menu(inv))
    assert pos is not None

def test_POS_menu_gives_the_dishes_with_prices():
    inv = make_random_dict()
    menu = make_menu(inv)
    pos = POS(0, inv.copy(), menu)
    customer_menu = {name: dish.price for name, dish in menu.items()}
    assert pos.menu() == customer_menu

def test_POS_balance_gives_current_balance():
    b = random_balance()
    pos = POS(b, {}, {})
    assert pos.balance() == b

def test_POS_inventory_returns_full_inventory():
    inv = make_random_dict()
    pos = POS(0, inv.copy(), make_menu(inv))
    assert pos.inventory() == inv

def test_POS_customer_order_is_valid_when_enough_ingredients():
    inv = make_random_dict()
    inv = {item: MAX_ITEM_COUNT for item in inv}
    menu = make_menu(inv)
    pos = POS(0, inv.copy(), menu)
    dish_name = random.choice(list(menu.keys()))
    assert pos.take_customer_order(dish_name)

def test_POS_customer_order_subtracts_from_inventory_for_valid_order():
    inv = make_random_dict()
    menu = make_menu(inv)
    dish_name, dish = random.choice(list(menu.items()))
    for i, a in dish.ingredients.items():
        inv[i] += a
    pos = POS(0, inv.copy(), menu)
    expected_inv = inv.copy()
    for i, c in dish.ingredients.items():
        expected_inv[i] -= c
    pos.take_customer_order(dish_name)
    
    assert pos.inventory() == expected_inv

def test_POS_customer_order_adds_price_to_balance_for_valid_order():
    inv = make_random_dict()
    menu = make_menu(inv)
    dish_name, dish = random.choice(list(menu.items()))
    # ensure that the dish is always valid
    for i, a in dish.ingredients.items():
        inv[i] += a
    price = dish.price
    pos = POS(0, inv.copy(), menu)
    pos.take_customer_order(dish_name)
    assert close_enough(pos.balance(), price)

def test_POS_customer_order_fails_when_not_enough_ingredients():
    inv = make_random_dict()
    menu = make_menu(inv)
    inv = {item: 0 for item in inv}
    pos = POS(0, inv.copy(), menu)
    dish_name = random.choice(list(menu.keys()))
    assert not pos.take_customer_order(dish_name)

def test_POS_customer_order_does_nothing_when_not_enough_ingredients():
    inv = make_random_dict()
    menu = make_menu(inv)
    inv = {item: 0 for item in inv}
    balance = random_balance()
    pos = POS(balance, inv.copy(), menu)
    dish_name = random.choice(list(menu.keys()))
    pos.take_customer_order(dish_name)

    assert pos.balance() == balance
    assert pos.inventory() == inv
    
def test_POS_customer_order_returns_false_on_invalid_order():
    inv = make_random_dict()
    menu = make_menu(inv)
    pos = POS(0, inv.copy(), menu)
    bad_order = make_bad_key(menu)
    assert not pos.take_customer_order(bad_order)

def test_POS_customer_order_does_nothing_on_invalid_order():
    inv = make_random_dict()
    menu = make_menu(inv)
    balance = random_balance()
    pos = POS(balance, inv.copy(), menu)
    bad_order = make_bad_key(menu)
    pos.take_customer_order(bad_order)

    assert pos.balance() == balance
    assert pos.inventory() == inv

def test_POS_restock_stocks_requested_items_on_valid_order():
    inv = make_random_dict()
    menu = make_menu(inv)
    cat = make_catalogue(inv)
    # ensure there are enough funds
    bal = sum(price * MAX_ORDER_SIZE for price in cat.values())
    order = make_order(cat)
    pos = POS(bal, inv.copy(), menu)
    pos.place_restock_order(order, cat)
    expected_inv = {i: a + (order[i] if i in order else 0) for i, a in inv.items()}
    expected_inv |= {i: a for i, a in order.items() if i not in inv}
    assert pos.inventory() == expected_inv

def test_POS_restock_stocks_only_valid_items():
    inv = make_random_dict()
    menu = make_menu(inv)
    cat = make_catalogue(inv)
    bal = sum(price * MAX_ORDER_SIZE for price in cat.values())
    order = make_order(cat)
    bad_order = order | {make_bad_key(cat): 1 for _ in range(5)}
    pos = POS(bal, inv.copy(), menu)
    pos.place_restock_order(bad_order, cat)
    expected_inv = {i: a + (order[i] if i in order else 0) for i, a in inv.items()}
    expected_inv |= {i: a for i, a in order.items() if i not in inv and i in cat}
    assert pos.inventory() == expected_inv

def test_POS_restock_fails_when_not_enough_funds():
    inv = make_random_dict()
    menu = make_menu(inv)
    cat = make_catalogue(inv)
    order = make_order(cat)
    # Ensure not enough funds, but greater than 0
    bal = sum(a * cat[i] for i,a in order.items()) / 2
    pos = POS(bal, inv.copy(), menu)
    assert not pos.place_restock_order(order, cat)
    # Check trivial case, just to be safe
    pos = POS(0, inv.copy(), menu)
    assert not pos.place_restock_order(order, cat)

    




if __name__ == "__main__":
    functions = inspect.getmembers(sys.modules[__name__], inspect.isfunction)
    test_functions = [f for f in functions if f[0].startswith("test_")]

    for name, test in test_functions:
        test_name = name[5:]
        class_name = test_name.split("_")[0]
        try:
            test()
        except AttributeError as e:
            if e.obj.__class__.__name__ == class_name:
                print(blue("Skipping {}. {}.{} does not appear to be implemented.").format(test_name, class_name, e.name))
            else:
                raise e
        except AssertionError as a:
            _, _, tb = sys.exc_info()
            tb_info = traceback.extract_tb(tb)
            _, line, _, text = tb_info[-1]
            message = red("Test '{}' failed.")
            if len(a.args) > 0:
                print((message+ " {}.").format(test_name, a.args[0]))
            else:
                print(message.format(test_name))
            print("> " + text.split(",")[0])
        except Exception as e:
            print(red("Test '{}' failed.").format(test_name))
            traceback.print_exc()
        else:
            print(green("Test '{}' passed").format(test_name))
            
