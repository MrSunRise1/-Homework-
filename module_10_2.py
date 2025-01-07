from random import randint
from threading import Thread
from queue import Queue
from time import sleep


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None
class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables: Table):
        self.tables = tables # столы в этом кафе
        queue = Queue() #объект класса Queue
    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            free_table = None
            for table in self.tables:
                if table.guest is None:
                    free_table = table
                    break
            if free_table:
                free_table.guest = guest
                guest.start()
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")
    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None
                        if not self.queue.empty() and table.guest is None:
                            visitor = self.queue.get()
                            table.guest = visitor
                            print(f"{visitor.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                            visitor.start()


tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()