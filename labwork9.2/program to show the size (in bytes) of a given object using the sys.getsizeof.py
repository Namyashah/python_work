import sys
def namya(object):
    result = sys.getsizeof(object)
    print(f"The Size of the Given Object is : {result}")
namya(42)
namya(3.14)
namya("Hello World")