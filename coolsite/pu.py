class asd():
    aaa=1
    def __init__(self, a, b) -> None:
        print(a,b)
        self.__fuc('777')
    def __fuc(self,z):
        print('111',z)

a = asd(22,33)
a.bbb = 555
print(a.aaa)