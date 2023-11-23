#Создайте класс Черепашка, который хранит позиции x и y черепашки,
#а также s - количество клеточек, на которое она перемещается за ход
#у этого класс есть методы:
#go_up() - увеличивает y на s
#go_down() - уменьшает y на s
#go_left() - уменьшает x на s
#go_right() - увеличивает y на s
#evolve() - увеличивает s на 1
#degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
#count_moves(x2, y2) - возвращает минимальное количество действий, 
#за которое черепашка сможет добраться до x2 y2 от текущей позиции

class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 1:
            raise ValueError("s не может быть меньше или равен 0")
        else:
            self.s -= 1

    def count_moves(self, x2, y2):
        return abs(x2 - self.x) + abs(y2 - self.y)
