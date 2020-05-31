def printTeacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

printTeacher(name='Ashley', job='Student', topic='Python')
