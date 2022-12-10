# Задание 3: Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.

with open('text before compression.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст для сжатия: '))
with open('text before compression.txt', 'r') as file:
    txt = file.readline()
    txt_compr = txt.split()  

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

txt_compr = coding(txt)

with open('text after compression.txt', 'w', encoding='UTF-8') as file:
    file.write(f' {txt_compr}')
print(f'Текс после сжатия:  {txt_compr}')    

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res    

txt_compr1 = decoding(coding(txt))

with open('text after recovery.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_compr1}')
print(f'Текст после восстановления: {txt_compr1}')  