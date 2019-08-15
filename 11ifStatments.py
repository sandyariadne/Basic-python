is_male = True

if is_male:
    print("You are a male")
else:
    print("You are a not male")

print("#####################################################")

isMale = True
isTall = True

if isMale or isTall :
    print("You are a male or tall or both")
else:
    print("You neither male non tall")

isMale1 = False
isTall1 = False

if isMale1 and isTall1 :
    print("You are a tall male")
else:
    print("You are either not male not tall or both")

print("#####################################################")

Male = True
Tall = False

if Male and Tall:
    print("You are a tall male")
elif Male and not(Tall):
    print("You are a short male")
elif not(Male) and Tall:
    print("You are not male but are tall")
else:
    print("You are not male and not tall")

print("####################COMPARISON#######################")

def mx_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(mx_num(23, 43, 41))