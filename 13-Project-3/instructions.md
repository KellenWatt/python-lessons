# Project 3 - The Restaurant

Here we are! The last gate! The Big Bad! The final exam! In this project, you'll be putting everything you've 
learned to use.

This project is intended to be significantly larger than anything you've written previously in these lessons. 
Whereas most of these projects and lessons were intended to take a few hours apiece, give or take (no shame if 
you took longer - being right is better than being quick), this project is designed to take longer, in part to 
give you a taste of what programming looks and feels like in the real world. Don't expect to do everything 
required in a single sitting. With that out of the way, story time!

> It seems like your inventory manager was a runaway hit! Not long after your client started using it, they came 
> to you with a big request: they want you to write software to manage their entire restaurant. You, really 
> wanting to get back to the series you've been watching, suggest that they should invest in a POS system, since 
> they already do that. But no, your client is insistent that you be the one to design it. They say that POS 
> systems don't do enough, but you think they just don't want to pay for someone else's software. You decide to 
> take it as a complement either way, and accept the job. 

Your task is to design 3 systems. Each of these will be described in greater detail below. Each of these
will be represented by a class.
#### Inventory/Kitchen Manager
You already did most of the heavy lifting for this one in the last project. In fact, if you did the optional 
exercise in the lesson on classes, you already did most of this one. To reiterate the requirements:
Make a class `Inventory` with the following methods:
- `use(name, count)` - subtract an item from inventory, 
if it exists and there is enough.
- `stock(name, count)` - add an item to inventory, 
even if it hasn't been ordered before.
- `amount(name)` - return the current amount of the item. If the item isn't in inventory, return `None`
- `is_stocked(name)` - return a boolean indicating it the item is in stock or not.
- `has_enough(name, count)` - return a boolean indicating if there are at least `count` items in stock.
- `in_history(name)` - return a boolean indicating if the item has ever been stocked.
- `current_inventory()` - returns a dictionary of the items currently in stock, including amounts
- `full_inventory()` - returns a dictionary of all items, both in and out of 
stock

Additionally, `Inventory` will have a constructor that takes a dictionary representing the current inventory.

#### Finance Manager
Any good business needs some way to track their expenses. You will 
make a class `Finance` with the following methods:
- `debit(amount)` - Deducts `amount` from the current balance, doing nothing if there is not enough. Returns a boolean for whether the transaction occurred.
- `credit(amount)` - Adds `amount` to the current balance.
- `balance()` - returns the current balance
- `enough_funds(amount)` - returns a boolean indicating if the balance is equal to or larger than `amount`
- `transaction_log()` - returns a list of the previous valid transactions, as numbers. Debits will be negative, and credits will be positive. The first transaction should be first, and the most recent last.

You will also need a constructor that takes a non-negative number, 
indicating the current balance.

`amount` will always be a positive number, but not necessarily an integer.

#### Point of Service (POS) system
The POS system will manage the other two systems, as well as customer 
orders. You will make a class `POS` with the following methods.
- `take_customer_order(dish)` - if inventory is available, and dish is on menu, subtract the inventory, according 
to the ingredients, and add the profit to the finance manager. Returns `True` on success, `False` otherwise.
- `place_restock_order(items, catalogue)` - add items to inventory, if there is enough money to pay for it, according to the 
finance manager. If an item is not in the catalogue, skip over it. Do nothing if there are not enough funds. 
Prices are gotten from the catalogue(key: ingredient name, value: cost). Returns `False` if the order fails completely, `True` otherwise.
- `menu()` - returns the restaurant's menu as a dictionary (key: dish name, value: price).
- `inventory()` - returns the full inventory, including items that 
are out of stock (key: item name, value: amount).
- `balance()` - returns the current balance of finance.

You will need a constructor that takes the following items as a parameters: 
- a non-negative number indicating current restaurant balance
- a dictionary representing the current inventory (key: item name, value: item amount)
- a dictionary representing the customer menu (key: dish name, value: class with two fields, `price` and `ingredients`(key: ingredient name, value: amount required))

You will not need to create the class used for dishes. It will be supplied in testing. You just have 
to treat it like it already exists.

Do not repeat the code used in the previous two classes to solve the same problems as before. Instead, use the classes 
themselves to control the parts of the POS system that they should reasonably manage (e.g. Finance manager should handle 
everything to do with the restaurant's balance).

### New Concepts
#### Relative Imports

When working with multiple files, as you will be in this project, you need some way for the code you wrote 
to be accessible from the others. This is where you can use *relative imports*. Normally, when you import 
something, you're importing a whole module that Python finds by being clever (i.e. we won't go into how this 
works). However, to import a file nearby, you can treat it the same way, as long as it doesn't have the same 
name as core library.

To access a file in the same directory (folder), all you need to do is write its name, minus the `.py` extension.
So to import `foo.py` in the same folder as what you're writing, you can just write `import foo`. To import a 
file in a subdirectory (folder lower than current one), you can write the name of the directory it's in, followed 
by a dot (.), and the name of the file you want to import. Repeat the folder + . for each level of folder you need. 
For example, to access `bar.py` in folder `foo`, you'll write `import foo.bar`.

To access things from that file you import, you access it the usual way. However, if you are accessing a 
file in a directory, you will need to write the full name, including the folder. So if `bar.py` has a function 
called `baz`, you would need to write `foo.bar.baz()` even after you import it.

#### Import Renaming

If the name you're importing is too long or complicated, you can change the name you use to refer to the module.
This is often useful for abbreviating long module names (including relative imports) or names you use often.
You do this by writing `as` and then the name you want to use after your `import` statement.
For example, in the `foo.bar` example above, if you only wanted to refer to the module as `bar` in your code, 
you could write `import foo.bar as bar`. Now, you only need to write `bar` to access things from `foo.bar`. 
As a note, don't just change the name to save a few keystrokes, unless the abbreviated name is just as clear 
as the longer one. 