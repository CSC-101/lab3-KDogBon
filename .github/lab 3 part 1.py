more = [x+1 for x in [2,2,3,4]]
print()


'''

x =			
1	2	3	4
X+1= 2	X+1= 3	X+1= 4	X+1= 5

More = [2,3,4,5]

'''




def square(x:int) -> int:
    return x*x


squares = [square(x) for x in [1,2,3,4]]
print()

'''
x =			
1	2	3	4
Square(x)= 1	Square(x)= 4	Square(x)= 9	Square(x)= 16
squares = [1,	4,	9,	16]


'''





def check(n:int) -> bool:
    return n>2

answer = [x for x in range(5) if check(x)]
print()

'''
n =			
1	2	3	4
check(n) = false	check(n) = false	check(n) = true 	check(n) = true
answer = [false,	False,	true,	true]

'''




def inc(m:int)->int:
    return m+1

def check(n:int)->bool:
    return n>2

answer2 = [inc(x) for x in range(5) if check(x)]
print()

'''

m =			
1	2	3	4
If check(n)			
N = 1	N = 2	N = 3	N = 4
false	false	true	true
inc(x) = 	inc(x)	inc(x) = 3	inc(x) = 4
		answer2 = [4,5]


'''