class Buffer:
    def __init__(self):  # конструктор без аргументов
        self.sequence = []

    def add(self, *a):  # добавить следующую часть последовательности
        for self.i in a:
            self.sequence.append(self.i)
        while len(self.sequence) >= 5:
            print(sum(self.sequence[0:5]))
            if len(self.sequence) == 5:
                self.sequence = []
            else:
                self.sequence = self.sequence[5:]

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        return self.sequence
