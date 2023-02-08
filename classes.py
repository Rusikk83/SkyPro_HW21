from abc import ABC, abstractmethod, abstractproperty


class Storage(ABC):

    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        available_count = self.get_free_space()
        if available_count < count:
            count = available_count
        if name in self.items.keys():
            self.items[name] += count
        elif count > 0:
            self.items[name] = count

    def remove(self, name, count):
        if self.items.get(name):
            if self.items.get(name) > count:
                self.items[name] -= count
            else:
                self.items.pop(name)

    def get_free_space(self):
        return  self.capacity - sum(list(self.items.values()))

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(set(self.items.keys()))


class Shop(Storage):
    def __init__(self):
        self.items = {}
        self.capacity = 100

    def add(self, name, count):
        if self.get_unique_items_count() >= 5:
            return None
        available_count = self.get_free_space()
        if available_count < count:
            count = available_count
        if name in self.items.keys():
            self.items[name] += count
        elif count > 0:
            self.items[name] = count

    def remove(self, name, count):
        if self.items.get(name):
            if self.items.get(name) > count:
                self.items[name] -= count
            else:
                self.items.pop(name)

    def get_free_space(self):
        return  self.capacity - sum(list(self.items.values()))

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(set(self.items.keys()))


class Request:
    def __init__(self, str_req):
        route = str_req.split(' ')
        self.from_ = route[4]
        self.to = route[6]
        self.amount = int(route[1])
        self.product = route[2]

    def __repr__(self):
        return f"from {self.from_} to {self.to} {self.amount} {self.product}"



sklad1 = Shop()

sklad1.add('soke', 2)

sklad1.add('cola', 3)

sklad1.add('soke1', 10)
sklad1.add('soke2', 10)
sklad1.add('soke3', 10)
sklad1.add('soke4', 10)

sklad1.remove('soke', 400)

print(sklad1.get_items(), sklad1.get_free_space(), sklad1.get_unique_items_count())

req = Request('Доставить 3 печеньки из склад в магазин')

print(req)