def num_translate(eng):


    nums = { 'zero' : 'ноль',
             'one' : 'один',
             'two' : 'два',
             'there' : 'три',
             'four' : 'четыре',
             'five' : 'пять',
             'six' : 'шесть',
             'seven' : 'семь',
             'eight' : 'восемь',
             'nine' : 'девять',
             'ten' : 'десять'}
    return nums.get(eng)
print(num_translate('eight'))
print(num_translate(input("Input an English nu,ber:")))
