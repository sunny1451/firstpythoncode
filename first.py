#login page for my college

def Login():
    print('enter the password:')
    password = input()
    if password == '12345':
        print('login sucessfull')
    else:
        print('pless enter the corrrect passwd')
    

print('enter your user name:')
name=input()
if name == 'sunny':
    Login()
else:
    print('the username you entered is wrong')
    print('pless enter the correct username')
    
