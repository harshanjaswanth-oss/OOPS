class Private:
    __privatevar=104
    def __private(self):
        print("This is a private method")
    def hello(self):
        print(Private.__privatevar)
obj=Private()
obj.hello()
obj.__private()
