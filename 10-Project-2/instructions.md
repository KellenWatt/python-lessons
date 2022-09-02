# Project 2 - Inventory Manager

Congratulations! You've done a lot of work and made a lot of progress! At this point, we've covered everything 
you absolutely *need* to know in order to write almost any program. But we won't make you write anything as hard 
as an operating system... yet. We've still got a few more things to cover that will make your life easier. But 
enough of this - back to the restaurant!

Our last little venture into automating our restaurant was a huge success! People are loving how easy it is to 
figure out what their tip is. Now your boss wants you to create a system to make an inventory management system. 
They say it'll make everything more efficient, but you think it probably has something to do with the fact the 
person who usually handles it has terrible handwriting. Either way, it's a net benefit, so it's time to get to work!

Your task is to write a series of functions that will manage the restaurant's inventory. These functions will be:
- `use_item(inventory, item, count)` - subtract an item from inventory, if it exists and there is enough
- `stock_item(inventory, item, count)` - add an item to inventory, even if it hasn't been ordered before
- `item_amount(inventory, item)` - return the current amount of the item
- `is_stocked(inventory, name)` - return a boolean indicating if the item is in stock or not
- `has_enough(inventory, name, count)` - return a boolean indicating if there are at least `count` of the item
- `in_history(inventory, name)` - return a boolean indicating if the item has ever been stocked
- `current_inventory(inventory)` - returns a list of the items that are currently in stock, regardless of amount
- `report(inventory)` - returns a string that lists the complete inventory, including amounts, with each item on its own line.

In each case, `inventory` is a dictionary that contains the restaurant's inventory. You don't need to worry about 
how you get it; you just have it. `name` will always be a string that is the name of the item relevant to 
that function. Inputs for `name` may or may not exist in `inventory` already, so you'll have to handle this. 
`count` is an integer indicating the relevant amount of the specific item. You can assume all counts will be non-negative, 
but don't assume the input is automatically valid for the given inventory.

You'll be modifying the `manager.py` file. Don't mess with any of the other files, since they're how they 
your code will be graded.

For any functions that modify the inventory, you will modify `inventory` directly. Don't worry about returning a new 
dictionary each time. Refer to the examples for more details about how each function more specifically behaves. In 
addition to the required functions, you're free to write any functions that you think will help you finish the project.
Only the required functions listed above will be tested.


### New Concepts
#### Escape Sequences

Remember the whole "there's no magic in programming" thing. That rule holds true for text. This means that since strings 
are just a bunch of characters, and strings can represent all text, then all text must be representable as a bunch of characters, 
including whitespace. If you think about it, something has to tell the computer to tab, or to go to 
the next line. We can't do that with any single key on the keyboard, since that will actually insert the thing 
we're trying to represent, and display and representation are often two different things when programming. To print these 
*special characters*, we have to use something called an *escape sequence*. Despite its fancy name, it's pretty simple. 
All you do is, inside a string, put a backslash ("\\"), followed by a character indicating what special character you want to insert. 
There are several sequences, some of them existing purely for historical reasons, but the most common ones you'll use are as follows.
- `\n` - newline. This is the character entered whenever you press Enter/Return on the keyboard
- `\t` - tab. Inserts a tab character, which takes you to the next *tabstop*
- `\\` - backslash. Inserts a literal backslash, instead of an escape sequence
- `\"` - double quote. Inserts a literal double quote. Useful when you want one in a string literal surrounded by double quotes
- `\'` - single quote. Same as double quote, but with single and double swapped.

For more information on this and how text works in general, you can read up on the ASCII and Unicode/UTF-8 standards. 
These are the rules modern computers use to encode human-readable text in a way that the machine can understand.

## Examples
Each of these examples will be based on the following inventory dictionary. This won't necessarily be the dictionary 
actually used in testing. Each of these examples is cumulative, so effects one will affect ones after.
```python
inventory = {
    "banana": 50,
    "kiwifruit": 143,
    "red bell pepper": 8,
    "eggs": 89,
    "garlic": 12
}
```

```python
use_item(inventory, "banana", 4)
# inventory now has "banana": 46
use_item(inventory, "garlic", 12)
# inventory now has "garlic": 0
use_item(inventory, "banana", 50)
# `use_item` does nothing, since there aren't enough bananas
use_item(inventory, "bananas", 5)
# `use_item` does nothing, since "bananas" isn't in the list (note the "s")
```

```python
stock_item(inventory, "kiwifruit", 100)
# inventory now has "kiwifruit": 243
stock_item(inventory, "dragonfruit", 20)
# inventory now has "dragonfruit": 20 (dragonfruit wasn't stocked before)
```

```python
item_amount(inventory, "red bell pepper")
# returns 8
item_amount(inventory, "garlic")
# returns 0
item_amount(inventory, "green bell pepper")
# returns None, since the item isn't stocked and never has been
```

```python
is_stocked(inventory, "eggs")
# return True
is_stocked(inventory, "egg whites")
# returns False
is_stocked(inventory, "garlic")
# returns False
```

```python
in_history(inventory, "banana")
# returns True, since currently in stock
in_history(inventory, "garlic")
# returns True, since has been ordered even if currently out
in_history(inventory, "onion")
# returns False, since never ordered or in inventory)
```

```python
has_enough(inventory, "banana", 30)
# returns True (30 < 46)
has_enough(inventory, "red bell pepper", 10)
# returns False (10 > 8)
has_enough(inventory, "jicama", 1)
# returns False, since not in inventory, therefore not enough
```

```python
current_inventory(inventory)
# returns ["banana", "kiwifruit", "red bell pepper", "eggs", "dragonfruit"] (not necessarily in that order)
# no garlic, since it's out of stock
```

```python
report(inventory)
# returns "banana: 46\nkiwifruit: 243\nred bell pepper: 8\neggs: 89\ngarlic: 0\ndragonfruit: 20\n"
# each "\n" is the escape sequence for newline. When printed, it should put a newline, 
# not literally print "\n"
```