#Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
#top_up(X) - пополнить на X
#count_1000() - выводит сколько целых тысяч осталось в кассе
#take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class CashDesk:
    def __init__(self, amount):
        self.amount = amount
    
    def top_up(self, x):
        self.amount += x
    
    def count_1000(self):
        return self.amount // 1000
    
    def take_away(self, x):
        if x <= self.amount:
            self.amount -= x
        else:
            raise ValueError("Недостаточно денег в кассе!")
