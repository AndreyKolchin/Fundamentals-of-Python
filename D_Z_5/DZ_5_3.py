from itertools import zip_longest


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


result = ((i, j) for i, j in zip_longest(tutors, klasses[:len(tutors)]))
print(type(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))