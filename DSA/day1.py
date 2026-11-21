# numbers=[10,20,30,40,50]
# print(numbers)
# print("First element:",numbers[0])
# print("Second element:",numbers[-1])

# #traversing a list
# for num in numbers:
#     print(num)
# #using a loop to calculate a sum
# total=0
# for num in numbers:
#     total=total+num
# print("Total=",total)

#Print every number and find largest
list1=[12,25,8,40,15]
sum=0
largest=list1[0]
smallest=list1[0]
for num in list1:
    print(num)
    sum=sum+num
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
print("sum=",sum)
print("Largest=",largest)
print("Smallest",smallest)
