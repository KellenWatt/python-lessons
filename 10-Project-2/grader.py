# This is the grader script for Project 2 - Inventory manager. This implements a basic testing framework
# from scratch. This is because at this point, the students don't know about libraries, and 
# requiring them to download pytest is just a distraction. This does not reflect good testing procedures, 
# and should not be used as a reference for such. This is purely a result of the limitations created 
# by not using a testing framework.


from operator import xor
import random
import string
import inspect
import sys
import string

assignment_functions = {
    "use_item": 3,
    "stock_item": 3,
    "item_amount": 2,
    "is_stocked": 2,
    "has_enough": 3,
    "in_history": 2,
    "current_inventory": 1,
    "report": 1
}
max_dict_size = 100
max_key_size = 20
max_quantity = 10000

def make_random_string(max_size = max_key_size):
    size = random.randint(1, max_size)
    return "".join([random.choice(string.ascii_letters) for i in range(size)])

def fuzz_dictionary(max_size = max_dict_size, max_count = max_quantity):
    size = random.randint(1, max_size) 
    return {make_random_string(): random.randint(0, max_count) for _ in range(size)}

def verify_signature(name, param_count):
    f = getattr(manager, name, None)
    if f is None:
        raise NameError("{} does not exist".format(name))
    sig = inspect.signature(f)
    if len(sig.parameters) != param_count:
        raise TypeError("{} needs {} parameters. Has {}".format(name, param_count, len(sig.parameters)))

def make_bad_key(dict):
    while True:
        bad_key = make_random_string()
        if bad_key not in dict: return bad_key

import manager.manager as manager



def test_item_amount():
    for _ in range(100):
        d = fuzz_dictionary()
        # normal use
        for k,v in d.items():
            assert manager.item_amount(d, k) == v 
        # key not in inventory, should return None
        for _ in range(10):
            bad_key = make_bad_key(d)
            assert manager.item_amount(d, bad_key) is None
    

def test_is_stocked():
    for _ in range(100):
        d = fuzz_dictionary()
        for k,v in d.items():
            if v > 0:
                assert manager.is_stocked(d, k)
            else:
                assert not manager.is_stocked(d, k)
        # key not in inventory, should always return False
        for _ in range(10):
            bad_key = make_bad_key(d)
            assert not manager.is_stocked(d, bad_key) 

def test_has_enough():
    for _ in range(100):
        d = fuzz_dictionary()
        for k,v in d.items():
            request = random.randint(1, max_quantity)
            if v >= request:
                assert manager.has_enough(d, k, request)
            else:
                assert not manager.has_enough(d, k, request)
        # key not in inventory, should always return False
        for _ in range(10):
            bad_key = make_bad_key(d)
            assert not manager.has_enough(d, bad_key, request)

def test_use_item():
    for _ in range(100):
        d = fuzz_dictionary()
        for k,v in d.items():
            request = random.randint(1, max_quantity)
            expected = v - request if request <= v else v
            manager.use_item(d, k, request)
            assert d[k] == expected
        # key not in inventory, inventory shouldn't be affected
        for _ in range(5):
            bad_key = make_bad_key(d)
            manager.use_item(d, bad_key, request)
            assert bad_key not in d 
                

def test_stock_item():
    for _ in range(100):
        d = fuzz_dictionary()
        for k,v in d.items():
            request = random.randint(1, max_quantity)
            expected = v + request
            manager.stock_item(d, k, request)
            assert d[k] == expected
        # key not in inventory, amount and key should be added as expected
        for _ in range(5):
            bad_key = make_bad_key(d)
            request = random.randint(1, max_quantity)
            expected = request
            manager.stock_item(d, bad_key, request)
            assert d[bad_key] == expected

def test_in_history():
    for _ in range(100):
        d = fuzz_dictionary()
        for k in d:
            assert manager.in_history(d, k)
        # key not in inventory, should return False
        for _ in range(10):
            bad_key = make_bad_key(d)
            assert not manager.in_history(d, bad_key)

def test_current_inventory():
    for _ in range(100):
        d = fuzz_dictionary()
        assert set(d) == set(manager.current_inventory(d))

def test_report():
    for _ in range(100):
        d = fuzz_dictionary()
        expected =  {"{}: {}".format(k,v) for k,v in d.items()}
        output = set(manager.report(d).rstrip().split("\n"))
        assert output == expected


if __name__ == "__main__":

    for name in assignment_functions:
        test_name = "test_" + name
        try:
            verify_signature(name, assignment_functions[name])
            getattr(sys.modules[__name__], test_name)()
        except NameError as e:
            print("{} skipped. Reason: {}.".format(test_name, e))
        except TypeError as e:
            print("{} skipped. Reason: {}.".format(test_name, e))
        except AssertionError as e:
            print("{} failed because of incorrect output".format(name))
        else:
            print("{} passed".format(name))



