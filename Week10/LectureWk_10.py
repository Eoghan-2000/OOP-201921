# #Pass by object reference
# # foo(bar)
# # What happens with bar depends on what type 'bar' is
# # if bar=13
# # name bount to the object is bar
# # 13 is the object
# # if bar is a mutable data type we see the difference everywhere
# # if not python creates a copy of this variable and passes it into the function
# # Mutable data types -> list
# a = 2
# # 2 is the object and a is the name bound to it
# print("a at beginning: ",id(a))
# a=a+1
# print("a after assinment: ",id(a))
# # when you increment a the name is not bound to the object two, it is now bound to the object 3
# # This means that there is a new location of a
#
# b=2
# print("new name b: ",id(b))
# #because be is assigned the object value 2, b now has the memory location that a had at the beginning
# # The Namespace of a variable
# # The space that the name exists in
# # they all have a scope

# def outer_function():
#     a=20
#
#     def inner_function():
#         a=30
#         print("INNER a:", a)
#     inner_function()
#     print("OUTER a: ", a)
#
#
# a=10
# outer_function()
# print("NO FUNCTION a: ", a)
# def change_me(A):
#     print("inside the function")
#     A=2
#     # B[0]='mutable'
#     B = [1,1]
#     # return A
# A=1
# B=[1,2]
# A= change_me(A)
# # print("A :", A, " B: ", B)
# print(A)

# This is because A is immutable
# B will not be reassigned to [1,1] because lists are not mutable as a whole but their contents are mutable individually
#
# some_guy="Fred"
# some_guy="George"
#
# # print(some_guy)
# first_names = []
# first_names.append(some_guy)
#
# # print(some_guy is first_names[0])
# # They both point to the same memory location because they are the names bound to the object George
#
# print("before Assignemnt: ", first_names)
# another_list_of_names = first_names
# another_list_of_names.append("Fred")
# print(first_names, another_list_of_names)
# this is becayse another_list... is assigned to the same object as first_names, so when you append one the other will change too