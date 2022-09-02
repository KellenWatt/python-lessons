# Expected functions
# - use_item(inventory, item, count)
# - stock_item(inventory, item, count)
# - item_amount(inventory, item)
# - is_stocked(inventory, name)
# - has_enough(inventory, name, count)` - return a boolean indicating if there are at least `count
# - in_history(inventory, name)
# - current_inventory(inventory)
# - report(inventory)

import random
import string
from inspect import signature


def make_random_string(max_size):
    size = random.randint(1, max_size)
    return "".join([random.choice(string.ascii_letters) for i in size])


def verify_signatures(f, param_count):
    sig = signature(f)
    assert len(sig.parameters) == param_count

import manager.manager as manager

def verify_assignment():
    manager.hello()

verify_assignment()
