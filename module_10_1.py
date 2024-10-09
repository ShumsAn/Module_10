from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name,'w', encoding='utf-8') as file:
        for i in range(1,word_count+1):
            file.write(f'\nКакое-то слово №{i}')
            sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")
#1.Обычный тест вызов функции 4 раза
start_time1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time1 = datetime.now()
time_one = end_time1 - start_time1
print(f'Работа потоков в первом тесте составила {time_one}')

#2.Создание потоков тест 2
start_time2 = datetime.now()
test_one = Thread(target=write_words,args=(10,'example5.txt'))
test_two = Thread(target=write_words,args=(30,'example6.txt'))
test_three = Thread(target=write_words,args=(200,'example7.txt'))
test_four = Thread(target=write_words,args=(100,'example8.txt'))

test_list = [test_one,test_two,test_three,test_four]
for i in test_list:
    i.start()
for k in test_list:
    k.join()

end_time2 = datetime.now()
time_two = end_time2 - start_time2
print(f'Работа потоков во втором тесте составила {time_two}')





