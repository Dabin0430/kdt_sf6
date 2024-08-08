#재귀함수 - 자기 자신을 호출하는 함수

def sos(n):
    print("Help me!!")
    if n == 1:
        return ""
    else:
        return sos(n-1)

'''
sos(5)
n=5, Help me!
sos(4)
n=4, Help me!
sos(3)
n=3, Help me!
sos(2)
n=2, Help me!
sos(1)
n=1, Help me!
'''
sos(1)

#팩토리얼 계산
def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n-1)
'''
4! = 4 * 3 * 2 * 1(팩토리알)
4! = 4 * (4-1)! 
3! = 3 * (3-1)! 
2! = 2 * (2-1)! 
1! = 1 * (1-1)! 
'''

#1 1 2 3 5 8 13