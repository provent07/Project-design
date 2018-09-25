# 1.	Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
# def max_of_three(a,b,c):
#     list=[a,b,c]
#     print(max(list))
#max_of_three(1,4,8)

# # 2.	Define a function that computes the length of a given list or string.
# list=[1,2,3,4,5]
# string="testing"
# def function(list):
#     return(sum(1 for i in list))
# print(function(list))
# def function(string):
#     return(sum(1 for i in string))
# print(function(string))

# 3.	Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
# alpha=input("Input alphabet: ")
# def function(alpha):
#     if alpha=='a'or alpha=='i'or alpha=='u'or alpha=='e'or alpha=='o':
#         print("True")
#     else:
#         print("False")
# function(alpha)

# 4.	Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I".
# test=input("Input word: ")
# def reverse(test):
#     print(test[::-1])
# reverse(test)

# 5.	Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)
# x=input("Input one anything: ")
# a=['a','i','u','e','o','1','2','3','4','5']
# def is_member(x,a):
#     for i in a:
#         if x==i:
#             print("True")
#             break
#     else:
#         print("False")
# is_member(x,a)

# 6.	Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.
# list1=[1,2,3,9]
# list2=[4,5,6,7]
# def overlapping():
#     for i in list1:
#         for j in list2:
#             if i==j:
#                 return True
#     return False
# print(overlapping())

# 7.	Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)
# num=int(input("Put input: "))
# alph=input("Put character: ")
# def generate_n_chars(num,alph):
#     return alph*num
# print(generate_n_chars(num,alph))

# 8.	Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7])
# def histogram(a,b,c):
#     print('*'*a)
#     print('*'*b)
#     print('*'*c)
# histogram(3,4,5)

# 9.	Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.
# num=int(input("Input number: "))
# count=0
# list=[]
# while count<num:
#     string=input("Input word: ")
#     list.append(string)
#     count+=1
# list1=[]
# def function():
#     for i in list:
#         total=len(i)
#         list1.append(total)
#     return list1
# print(function())

# 10.	Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
# num=int(input("Input number: "))
# count=0
# list=[]
# while count<num:
#     string=input("Input word: ")
#     list.append(string)
#     count+=1
# list1=[]
# def find_longest_word():
#     for i in list:
#         total=len(i)
#         list1.append(total)
#         if total==max(list1):
#             a=max(list1)
#     return a
# print(find_longest_word())

# 11.	A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.
# sentence=input("Input sentence: ")
# def is_pangram():
#     c = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     phraseLetters = ""
#     for char in sentence:
#         for letter in alphabet:
#             if char == letter and char not in phraseLetters:
#                 phraseLetters += char
#     for char in phraseLetters:
#         for letter in alphabet:
#             if char == letter:
#                 c += 1
#     if c == 26:
#         return True
#     else:
#         print(phraseLetters, alphabet)
#         return False
#
# print(is_pangram())

# 12.In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going. Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its present participle form
# word=input("Put word: ")
# def make_ing_form():
#     words=list(word)
#     if words[-1]=='e' and words[-2]=='i':
#         words=words[:-2]
#         words.append('ying')
#         str1 = ''.join(words)
#         print(str1)
#     elif words[-1]=='e' and words[-2]!='i':
#         words.append('ing')
#         str1 = ''.join(words)
#         print(str1)
#     elif words[-2]=='a' or words[-2]=='i' or words[-2]=='u' or words[-2]=='e' or words[-2]=='o':
#         if words[-1]!='a' or words[-1]!='i' or words[-1]!='u' or words[-1]!='e' or words[-1]!='o':
#             if words[-3] != 'a' or words[-3] != 'i' or words[-3] != 'u' or words[-3] != 'e' or words[-3] != 'o':
#                 words.append(word[-1])
#                 words.append('ing')
#                 str1 = ''.join(words)
#                 print(str1)
#     else:
#         words.append('ing')
#         str1 = ''.join(words)
#         return str1
# make_ing_form()







