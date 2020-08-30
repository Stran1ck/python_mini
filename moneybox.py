class MoneyBox:
    def __init__(self, capacity, box=0):
        # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.box = box

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.capacity - self.box >= v:
            return True
        else:
            return False

    def add(self, v):
        # положить v монет в копилку
        if self.can_add(v):
            self.box += v
