from threading import Thread
from time import sleep
import queue
from random import randint

class Table:
    def __init__(self,number):
        self.number = number
        self.guest = None
class Guest(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        time_sleep = randint(3,10)
        sleep(time_sleep)

class Cafe():
    def __init__(self,*tables):
        self.q = queue.Queue()
        self.tables = tables
    def guest_arrival(self, *guests):
        for person in guests:
            flag = True
            for table in self.tables:
                if table.guest is None:
                    table.guest = person
                    person.start()
                    print(f"{person.name} сел(-а) за стол номер {table.number}")
                    flag = False
                    break
            if flag:
                self.q.put(person)
                print(f"{person.name} в очереди")

    def discuss_guests(self):
        for table in self.tables:
            if not self.q.empty() and table.guest.is_alive():
                print(f"{table.guest.name} покушал(-а) и ушел(ушла)")
                print(f"Стол номер {table.number} свободен")
                table.guest = None
            else:
                table.guest = self.q.get()
                print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                self.guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# # Заполнение кафе столами
cafe = Cafe(*tables)
# # Приём гостей
cafe.guest_arrival(*guests)





