print('Введи номер, с которого будет идти нумерация')
number = int(input())
while True:
    print('Введи текст')
    text = input()
    print('Введи жанр цифрой(Художественный - 0, научный - 1, публицистический - 2')
    genre = int(input())
    file_name = 'Sample_Text_' + str(number) + '.txt'
    file = open(file_name, 'r+')
    file.write(text)
    file.close()
    answer_name = 'Genre_' + str(number) + '.txt'
    file = open(answer_name, 'r+')
    if genre == 0:
        file.write('Художественный')
    elif genre == 1:
        file.write('научный')
    elif genre == 2:
        file.write('публицистический')