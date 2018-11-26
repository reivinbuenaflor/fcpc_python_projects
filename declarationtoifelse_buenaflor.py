print("Enter your First Name: ")
user_fName = input()
print("Enter your Last Name: ")
user_lName = input()
print("Enter your Age: ")
user_Age = input()
print("Enter your Birth Month: ")
user_bMonth = input()
print("Enter your Birth Date: ")
user_bDate = input()
print("Enter your Birth Year: ")
user_bYear = input()
print("Enter your gender: ")
user_gender = input()

if user_gender == "Male" or user_gender == "male":
    print(user_fName + user_lName)
    print(user_Age)
    print(user_bMonth + user_bDate + user_bYear)
    print(user_gender)
elif user_gender == "Female" or user_gender == "female":
    print(user_fName + user_lName)
    print(user_Age)
    print(user_bMonth + user_bDate + user_bYear)
    print(user_gender)
else:
    print("Undifined")

x = 30
y = 10
sum = x + y
diff = x - y
prod = x * y
quo = x / y
mod = x % y

print(sum)
print(diff)
print(prod)
print(quo)
print(mod)
