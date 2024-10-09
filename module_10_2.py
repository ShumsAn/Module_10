from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days_f = 0
        for i in range(1,enemies):
            sleep(1)
            enemies -= self.power
            days_f += 1
            print(f'{self.name} сражается {i} день(дня), осталось {enemies} воинов')
            if enemies == 0:
                break
        print(f'{self.name} одержал победу спустя {days_f} дней(дня)! ')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились')



