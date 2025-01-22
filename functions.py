# Double the value of a number.
# Input: a number to be doubled
# Result: a number
def double(n:int) -> int:
    result = 2 * n
    return result
'''
The problem with the code is that we were squaring the number instead of doubling it, so I swapped n*n to 2*n.

But for the question how many tests it would take to properly run, theoretically in a perfect world only 1 or none if it runs correctly. However, we often don’t live in a perfect world so it will probably take a couple of tests, or if you don’t catch it you will get backlash from your company or the public.

'''