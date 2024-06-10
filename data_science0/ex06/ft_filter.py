
class ft_filter:

    __doc__ = """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    def __init__(self, function, iterable):

        if '__iter__' not in dir(iterable):
            raise TypeError("TypeError: Not an iterable type")
        if function is None:
            self.returning_data = [x for x in iterable if x]
        else:
            self.returning_data = [x for x in iterable if function(x)]

    def __iter__(self):
        return iter(self.returning_data)

    def __repr__(self):
        return f'<ft_filter object at {hex(id(self))}>'

    def __str__(self):
        return self.__repr__()
