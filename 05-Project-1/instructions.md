# Project 1 - Tip Calculator

Good job making it this far! So far, if you've been doing these lessons in order, we've covered the basics of Python itself, 
as well as data types, variables, and basic logic. Now's the time to put these into practice. 

Your mission, should you choose to accept it, it to make a tip calculator. Your job is to prompt the user for the cost 
of the meal, and the number of patrons. You'll take the cost, then suggest the tip values for 15%, 20%, and 25%, listing 
each in order. If there are 8 or more patrons, a 20% tip should be automatically included, with a message saying as much.

Unlike the previous lessons, you will be writing your code in its own file, namely the `calculator.py` file provided. Don't
change the name of this file, as the grader script relies on it.

Your output messages should match the example provided below exactly. The grader script provided will expect to match 
those patterns exactly. Assume that both of the values given by the user are valid numbers, but don't assume that the bill 
amount entered will have exactly two decimal places. Don't worry about making the output have exactly two decimal places - 
this goes beyond the scope of this project. Don't use prompt messages for the inputs. You can assume they will 
be entered as expected.

### New Concepts
#### `round()`
It's often useful to be able to round a number to a given precision, especially when working with money. This is where the
`round` function is very convenient. If you give it a number (calling it the same way you would call `input`), it returns
the nearest whole number. If you also give it another value, separated by a comma, it will round to the nearest value 
with that many digits.

```python
round(3.1415)  # returns 3

round(3.1415, 2) # returns 3.14

round(4.2, 10) # return 4.2, since 4.2 has fewer than 10 decimal places.
```

## Examples

Input: 
```
100
2
```
Output:
```
Your tip options are:
15%: $115.0
20%: $120.0
25%: $125.0
```
---

Input:
```
100
8
```
Output:
```
A 20% tip is automatically added to parties of 8 or more. Your bill is $120.0.
```
---

Input:
```
30.64
5
```
Output:
```
Your tip options are:
15%: $35.24
20%: $36.77
25%: $38.3
```
---

Input:
```
87.388
12
```
Output:
```
A 20% tip is automatically added to parties of 8 or more. Your bill is $104.87.
```