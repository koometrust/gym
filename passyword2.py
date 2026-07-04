name = input('What is your name ?')
password = input('Password ?')
# plength = len(password)
# hash = '*' * plength
# print(name)
# print(password)
# print(plength)
# print(hash)


#print(f'hello {name} hope you\'re well yout password is {hash} & it has a length of {plength} characters ')
#Good Job Jude

if name == 'Jude' and password == '12345':
    State = True 
    access = 'granted'
    print(f'Password is {State} access is {access}')

else:
    State = False
    access = 'Denied'
    print(f'Password is {State} access is {access}')
