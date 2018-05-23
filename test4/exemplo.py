class class_name:
    def __init__(self, arg_1, arg_2, arg_3=None):
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self._arg_3 = arg_3


    def _private(self, value):
        pass

    def method_1(self):
        return self._private(arg_1)

    def method_2(self, value):
        return self.arg_2 * value

xerox = class_name('papel', 'ink', 'tonner')
print(xerox.arg_3)
