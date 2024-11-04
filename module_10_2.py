import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.vragi = 100
        self.days = 0



    def run(self):
        print(f"{self.name}, на нас напали!")
        days = 0
        while self.vragi > 0:
            time.sleep(1) #1 день проходит
            days += 1
            self.vragi -= self.power
            print(f"{self.name} сражается {days} дней..., осталось {self.vragi} воинов.")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

voin1 = Knight('Гриффит', 13)
voin2 = Knight('Берсерк', 9)
voin1.start()
voin2.start()

voin1.join()
voin2.join()