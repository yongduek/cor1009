vowel = ['a', 'e', 'i', 'o', 'u']
v2i = { v : str(i+1) for i, v in enumerate(vowel) }

print(v2i)

# i2v = {}
# for key, value in v2i.items():
#     print(key, value)
#     i2v[value] = key 

i2v = { value: key for key, value in v2i.items() }
print(i2v)
