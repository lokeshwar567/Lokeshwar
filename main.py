# def fun(x,y):
#     print(x,y)
#     return x+y
# print(fun(2,3))
# def fun(x,y):
#     return x*x+y*y
# print(fun(3,4))3
# for i in range(1,101):
#     if i%2!=0:
#         print(i)
#
# for i in range(0,2000):
# i=1996
# if i%4==0 and i%100!=0 or i%400==0:
#     print('leap year')
# else:
#     print('not a leap year')
# a=3
# for i in range(0,11):
#     print(a*i)
# l=[1]
# k=[2]
# print(id(l))
# print(id(k))
# s={1,2,4,5,6,8,1}
# print(s)
# a=10
# b=8
# c=40
# if a>b and a>c:
#     print("a is big")
# elif b>a and b>c:
#     print("b is big")
# else:
#     print("c is big")
# a=int(input("enter value"))
# if 91<=a<=100:
#     print("a grade")
# elif 81<=a<=90:
#     print("b grade")
# elif 71<=a<=80:
#     print("c grade")
# elif 61<=a<=70:
#     print("d grade")
# elif 51<=a<=60:
#     print("e grade")
# # elif 0<=a<=50:
# else:
#     print("fail")
# def fun(x,y):
#     z=x<<y
#     print(z)
# fun(3,1)
# def fun(x):
#     if x>=0:
#         print("positive")
#     else:
#         print("negetive")
# fun(3)
# def fun(*b):
#     print(b)
# fun(1,3,5,6,4,7,8)
# def fun(**b):
#     print(b['a'])
# fun(a=10,b=20,c=30)
# =1
# while(i<=100):
#     print(i)
#     i=i<<1
# print(i+2)
# i=100
# while(i>=1):
#     print(i+1)
#     i=i>>1
#     i=i-1
# print(i+10)
# map lamda filter reduce
# Formats
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count
# print(count_vowels("Hello World"))
# for i in range(1,101):
#     if i%2!=0:
#         print(i)
#
# for i in range(0,2000):
# i=1996
# if i%4==0 and i%100!=0 or i%400==0:
#     print('leap year')
# else:
#     print('not a leap year')
# a=3
# for i in range(0,11):
#     print(a*i)
# l=[1]
# k=[2]
# print(id(l))
# print(id(k))
# s={1,2,4,5,6,8,1}
# print(s)
# a=10
# b=8
# c=40
# if a>b and a>c:
#     print("a is big")
# elif b>a and b>c:
#     print("b is big")
# else:
#     print("c is big")
# a=int(input("enter value"))
# if 91<=a<=100:
#     print("a grade")
# elif 81<=a<=90:
#     print("b grade")
# elif 71<=a<=80:
#     print("c grade")
# elif 61<=a<=70:
#     print("d grade")
# elif 51<=a<=60:
#     print("e grade")
# # elif 0<=a<=50:
# else:
#     print("fail")
# def fun(x,y):
#     z=x<<y
#     print(z)
# fun(3,1)
# def fun(x):
#     if x>=0:
#         print("positive")
#     else:
#         print("negetive")
# fun(3)
# def fun(*b):
#     print(b)
# fun(1,3,5,6,4,7,8)
# def fun(**b):
#     print(b['a'])
# fun(a=10,b=20,c=30)
# =1
# while(i<=100):
#     print(i)
#     i=i<<1
# print(i+2)
# 1 def sum_even(a):
#     s = 0
#     for i in a:
#         if i%2==0:
#             s += i
#     return s
#
# def sum_odd(a):
#     s = 0
#     for i in a:
#         if i%2!=0:
#             s += i
#     return s
# li = list(map(int,input('enter numbers: ').split()))
#
# print("1. sum of odd numbers")
# print("2. sum of even numbers ")
#
# choice = int(input("enter your choice :"))
#
# if choice == 1:
#     print("sum of odd numbers:",sum_odd(li))
# elif choice == 2:
#     print("sum of even numbers:", sum_even(li))
# else:
#     print("invalid choice")
# def fun(**x):
#     print(x)
# a={'name': 'loki','roll':43,'marks': 100}
# b={'name': 'loi','roll':42,'marks': 10}
# fun(**a)
# fun(**b)
# celsius=[37,34,56,72]
# fahrenheit=map(lambda x:(x*1.8)+32,celsius)
# print(list(fahrenheit))
# names=['loki','lohith','raj']
# fl=map(lambda x:x[0],names)
# print(list(fl))
# names=['jashu','loki','lofert']
# vowel=filter(lambda x:(x[0] in ['a','e','i','o','u','A','E','I','O','U']),names)
# print(list(vowel))
# n=int(input('enter a number'))
# result= 'AB'*n
# print(result)
#32121
# a=[1,2,3,4]
# b=[10,20,30,40]
# nl=map(lambda x,y:x+y,a,b)
# print(list(nl))
# nums=[12,15,7,18,20,21,25]
# div3=filter(lambda x:x%3==0,nums)
# div5=filter(lambda x:x%5==0,nums)
# both=filter(lambda x:x%3==0 and x%5==0,nums)
# nb=filter(lambda x:x%3 or x%5,nums)
# print(list(div3))
# print(list(div5))
# print(list(both))
# print(list(nb))
