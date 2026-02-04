#caesar Cipher encryption

text = input('enter message: ')
shift = 3
encryption =' '
for char in text:
    encryption += chr(ord(char)+shift)

print('encrypted data:',encryption)

