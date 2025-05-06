#HFC

small_num=int(input("enter the smallest number "))
big_num=int(input("enter the largest number "))


while small_num:
    store_num=small_num
    small_num= big_num % small_num
    big_num = store_num

print("hcf is ", big_num)
