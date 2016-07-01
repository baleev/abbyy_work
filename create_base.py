print('Введи номер, с которого будет идти нумерация')
number = int(input())
while True:
    print('Введи текст (для выхода введи 0)')
    text = input()
    if text == '0':
        break
    print('Введи жанр цифрой(Художественный - 0, научный - 1, публицистический - 2)')
    genre = int(input())
    file_name = 'Sample_Text_' + str(number) + '.txt'

    #Добавил кодировку
    file = open(file_name, 'w', encoding='utf-8')

    file.write(text)
    file.close()
    answer_name = 'Genre_' + str(number) + '.txt'

    # Добавил кодировку и тут
    file = open(answer_name, 'w', encoding='utf-8')

    if genre == 0:
        file.write(u'Художественный')
    elif genre == 1:
        file.write(u'научный')
    elif genre == 2:
        file.write(u'публицистический')
    file.close()
    number += 1
