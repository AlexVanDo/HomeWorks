# Доработать класс FlatIterator в коде ниже.
# Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
# т.е. последовательность, состоящую из вложенных элементов.
# Функция test в коде ниже также должна отработать без ошибок.
class FlatIterator:

    def __init__(self, multi_list):
        self.multi_list = multi_list


    def __iter__(self):
        self.list_iter = iter(self.multi_list)
        self.some_list = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.some_list) == self.cursor:
            self.some_list = None
            self.cursor = 0
            while not self.some_list:
                self.some_list = next(self.list_iter)
        return self.some_list[self.cursor]  


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()