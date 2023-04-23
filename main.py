class Translator:
    tr_dct = {}

    def add(self, eng, rus):
        if rus not in self.tr_dct.get(eng, []):
            self.tr_dct.setdefault(eng, []).append(rus)

    def remove(self, eng):
        del self.tr_dct[eng]

    def translate(self, eng):

        return self.tr_dct[eng]

tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove('car')

print(*tr.translate('go'))