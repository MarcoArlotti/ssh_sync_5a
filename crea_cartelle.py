import os
for i in range(20):
    try:
        os.mkdir(f'arlotti_{i}')
    except:
        pass
        