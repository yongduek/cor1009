plain_text = "This is a test. ABC abc"
 
encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)

dec_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    dec_text = dec_text + c2

print(dec_text)

print(chr(0x10ffff))

print('한')
print(ord('한'), hex(ord('한')))
print(ord('가'), hex(ord('가')))
print(ord('ㄱ'), hex(ord('ㄱ')))


# dictionary data type == associative memory

a = ['x', 13, "string", [0, 1]]
#a[0]
#a[1]
#a[2]

# key, value
b = { '가': '한글의 첫 글자' ,  3: '숫자의 4번째',  5: 5*2 }

print( b['가'], b[3], b[5] )

for k in b.keys():
    print(k)