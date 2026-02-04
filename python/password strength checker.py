#password strength checker

password=input('enter the password: ')
if len(password) < 5:
    print('the password is so weak please change the password',password)
elif password.isdigit() or password.isalpha():
    print('mid password(use letters + numbers)')
else:
    print('thanks for the login')
    
