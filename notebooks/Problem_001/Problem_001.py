# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Problem 1
# ## Multiples of 3 or 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# %% slideshow={"slide_type": "slide"}
# Solution 1: straight forward loop checking

# Thought process:
#   1. Need to sum all numbers below a certain limit that are multiples of 3 or 5
#   2. Need to not waste memory allocation, therefore store value in variable 'sum'
#       (using list clutter local memory, especially when calling final sum as its a pointer object)
#   3. A number 'x' is divisible by 'y' iff x mod y = 0 (x % y == 0)
#   4. Recall the truth table for OR, sum those which are either divisible by 3 or 5.

# %% slideshow={"slide_type": "slide"}
LIMIT   = 10000
sum     = 0

for num_ in range(LIMIT):
    if not (num_ % 3) or not (num_ % 5):
        sum += num_

print(sum)
