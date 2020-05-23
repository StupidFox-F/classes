from timer import timer

class lazy_object:
    def __init__(self, callable, *args, **kw):
        self.__dict__['callable'] = callable
        self.__dict__['args'] = args
        self.__dict__['kw'] = kw
        self.__dict__['obj'] = None

    def initobject(self):
        if self.obj is None:
            self.__dict__['obj'] = self.callable(*self.args, **self.kw)

    def __getattr__(self, name):
        self.initobject()
        return getattr(self.obj, name)

    def __setattr__(self, name, value):
        if name == 'reset' and value == 1:
            self.__dict__['obj'] = None
        else:
            self.initobject()
            setattr(self.obj, name, value)

    def __len__(self):
        self.initobject()
        return len(self.obj)

    def __getitem__(self, idx):
        self.initobject()
        return self.obj[idx]


class A:
    def __init__(self, num_elem):
        self.attr1 = list(range(num_elem))
        self.reset = 0


a = lazy_object(A, num_elem=10 ** 7)


with timer('Elapsed: {}ms'):
    type(a.attr1)


with timer('Elapsed: {}ms'):
    type(a.attr1)

a.reset = 1

with timer('Elapsed: {}ms'):
    type(a.attr1)

with timer('Elapsed: {}ms'):
    type(a.attr1)

