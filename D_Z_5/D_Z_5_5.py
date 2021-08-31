from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
unig_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Source list\n{my_list}\nNo repetition list\n{unig_list}")

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [src[i] for i in range(len(src)) if src[i] not in src[i + 1:] and src[i] not in src[:i]]



