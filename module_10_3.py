from random import randint
from threading import Thread , Lock
from time import sleep

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
               self.lock.release()
            random_sum_d = randint(50,500)
            self.balance += random_sum_d
            print(f'"Пополнение: {random_sum_d}. Баланс: {self.balance}".')
            sleep(0.001)

    def take(self):
        for i in range(100):
            random_sum_t = randint(50,500)
            print(f'Запрос на {random_sum_t}')
            if random_sum_t <= self.balance:
                self.balance -= random_sum_t
                print(f'Снятие: {random_sum_t}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
