# class dictionary_iter:
#     def __init__(self, data):
#         self.items = list(data.items())
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.idx >= len(self.items):
#             raise StopIteration
#         result = self.items[self.idx]
#         self.idx += 1
#         return result

class dictionary_iter:
    def __init__(self, obj):
        self.obj = obj
        self.generator = (pair for pair in self.obj.items())

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.generator)


