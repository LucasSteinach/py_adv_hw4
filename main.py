nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

power_nested_list = [
    ['a', ['b', ['c', 'GGG']]],
    ['d', ['e', 'GG'], ['f', ['HH', 'III'], 'h'], False],
    [1, 2, None]
]
# TODO 1.Iterator for nested lists


class FlatIterator:
    def __init__(self, input_list: list):
        self.list = input_list
        self.end = len(self.list)

    def __iter__(self):
        self.cursor = 0
        self.item_cursor = 0
        return self

    def __next__(self):
        self.item_cursor += 1
        if self.cursor == self.end:
            raise StopIteration
        if self.item_cursor == len(self.list[self.cursor]):
            self.cursor += 1
            self.item_cursor = 0
            return self.list[self.cursor - 1][-1]
        return self.list[self.cursor][self.item_cursor - 1]


for item in FlatIterator(nested_list):
    print(item)


# TODO 2. Generator for nested lists.

def nested_generator(some_list: list):
    for item in some_list:
        i = 0
        while i < len(item):
            yield item[i]
            i += 1


for item in nested_generator(nested_list):
    print(item)


# TODO 3. Unlimited iterator

# class MegaFlatIterator:
#     def __init__(self, input_list: list):
#         self.list = input_list
#         self.end = len(self.list)
#
#     def __iter__(self):
#         self.cursor = 0
#         self.item_cursor = 0
#         return self
#
#     def __next__(self):
#         self.item_cursor += 1
#         if type(self.list[self.cursor][self.item_cursor]) == list:
#             for it_ in MegaFlatIterator(self.list[self.cursor][self.item_cursor - 1]):
#                 print(it_)
#         else:
#             if self.cursor == self.end:
#                 raise StopIteration
#             if self.item_cursor == len(self.list[self.cursor]):
#                 self.cursor += 1
#                 self.item_cursor = 0
#                 return self.list[self.cursor - 1][-1]
#         return self.list[self.cursor][self.item_cursor - 1]
#
#
# for item in MegaFlatIterator(power_nested_list):
#     print(item)


# TODO 4. Unlimited generator
