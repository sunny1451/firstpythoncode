#Brute Force Simulation

correct_password="1234"
password_list=['0000','2222','1234','2334']

for pwd in password_list:
    print('typing',pwd)
    if pwd == correct_password:
        print('password craked successfully',pwd)
        break
