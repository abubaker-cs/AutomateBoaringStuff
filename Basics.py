# The program says hello and asks for my name

print('Hello world!')

# Ask for the username
print('What is your name?')
userName = input()

# Print the username
print('It is good to meet you, ' + userName)
print('The length of your name is: ')
print(len(userName))

# Age
print('What is your age?')
userAge = input()
print('You will be ' + str(int(userAge) + 1) + ' in a year.')
