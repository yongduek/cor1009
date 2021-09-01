import numpy as np

np.random.seed(156)
students = ["nandita", 'sharon', '김예진', '유영서', '이준하', 
            '김규리', '이채은', '정어진', '이상민', '안예현']

selected = np.random.choice(students)
print(selected)
