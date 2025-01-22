def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num
    return total

result = tally([4,9,2,1])
print()
print(result)

'''
	
Sum of total

Line 3	Iteration 1	Iteration 2	Iteration 3	Iteration 4
           Num = 4	  Num = 9	 Num = 2	  Num =1

Line 4	Iteration 1	Iteration 2	Iteration 3	Iteration 4
        total = 4	total = 13	total = 15	total =16


'''


def copy (nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])
    return new_list

result = copy([4,9,2,1])

'''
	
copy()

Line 15	Iteration 1	Iteration 2	Iteration 3	Iteration 4
          idx = 0	idx = 1     idx = 2	    idx =3

Line 16	        Iteration 1	        Iteration 2	        Iteration 3	        Iteration 4
                New_list = [4]	   New_list = [4, 9]	New_list = [4, 9, 2]	 New_list = [4, 9, 2, 1,]

It creates a list you can alter without changing the other list

'''



def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for idx in nums:
        new_list.append(idx + 1)
    return new_list

result = increment_all([4,9,2,1])
print()


'''
	
copy

Line 15	Iteration 1	  Iteration 2	   Iteration 3	    Iteration 4
        idx = 4	       idx = 9    	idx = 2	          idx =1

Line 16	        Iteration 1 	    Iteration 2	         Iteration 3	          Iteration 4
                New_list = [5]	   New_list = [5, 10]	New_list = [5, 10, 3]	New_list = [5, 10, 3, 2]




'''