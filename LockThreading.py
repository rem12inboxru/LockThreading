import threading
from threading import Thread, Lock

lock = Lock()

class BankAccount(Thread):
    def __init__(self, account, ammount):
        threading.Thread.__init__(self)
        self.account = account
        self.ammount = ammount

    def deposit_task(self):
        for i in range(5):
            with lock:
                self.ammount += 100
                print(f'Пополнение на 100, новый баланс{self.ammount}')


    def withdraw_task(self):
        for i in range(5):
            with lock:
                self.ammount -= 150
                print(f'Снятие 150, новый баланс {self.ammount}')


account123 = BankAccount(123, 1000)

deposit_thread = threading.Thread(account123.deposit_task())
withdraw_thread = threading.Thread(account123.withdraw_task())

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
