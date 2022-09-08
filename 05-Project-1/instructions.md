# Project 1 - Tip Calculator

Good job making it this far! So far, if you've been doing these lessons in order, we've covered the basics of Python itself, 
as well as data types, variables, and basic logic. Now's the time to put these into practice. Story time!

Recently, a local restaurant owner reached out to you, since they heard you're an up-and-coming programmer, and they want 
to try and start automating parts of their business. That said, they haven't worked with you before, so you've agreed to 
start out with something small: a tip calculator. Your client figures that if people are presented with tip amounts, 
they'll be more willing to pay decent tips.

Your job is to take the cost of the meal, and the number of customers. You'll suggest tip values for 15%, 20%, and 25%, in 
order. If there are 8 or more customers on a single bill, a 20% tip will be automatically added, with a message saying as much.


Unlike the previous lessons, you will be writing your code in its own file, namely the `calculator.py` file provided. Don't
change the name of this file, as the grader script relies on it.

Your output messages should match the format of each of the examples provided below exactly. The grader script provided will 
expect to match those patterns exactly. Assume that both of the values given by the user are valid numbers, but don't assume 
that the bill amount entered will have exactly two decimal places. Don't worry about making the output have exactly two 
decimal places - this goes beyond the scope of this project. Don't use prompt messages for the inputs. You can assume they 
will be entered as expected.

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

#### `format()`
Putting your own information in a pre-existing string is a really common thing to do when you're making messages. So common,
in fact, that most (semi-)modern programming languages have some way of making it simpler. Python's version of this is the
`format` function. 

`format` is really easy to use. Whenever you want to insert something into your string later, like a number that changes 
between printings, you put a literal `{}` in its place in the string. Then, at the end of the string, you call the `format`
function, putting that value between the parentheses.

```python
luck_forecast = "Your lucky number is {}!"

luck_forecast.format(7) # returns "Your lucky number is 7!"
luck_forecast.format(13) # returns "Your lucky number is 13!"
```

You can also do this with multiple values. The values given to `format` will be inserted in the order given.
```python
countdown = "Launching in {}. {}. {}. Launch!"

countdown.format(3, 2, 1) # returns "Launching in 3. 2. 1. Launch!"
countdown.format(1, 2, 3) # returns "Launching in 1. 2. 3. Launch!"
# You can even mix up your data types. Python doesn't care!
countdown.format("三", "deux", 1) # returns "Launching in 三. deux. 1. Launch!"
```

Don't worry too much about the whole dot-between-the-variable-and-function thing. We'll talk more about those in 
future lessons, mentioning them when we talk about lists, and then covering it in-depth when we start talking about 
classes. For now, just know that you need to use it this way to make it work. This doesn't affect any of the other 
functions we've talked about so far.

## Example Cases

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