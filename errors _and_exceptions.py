# Exception handling

class TooHighValueError(Exception):
    pass


class TooLowValueError(Exception):
    def __init__(self, message, x):
        self.message = message
        self.x= x


class FunnyNumberError(Exception):
    def __init(self, number, message):
        self.number = number
        self.message = message

x:int = int(input("please give a number"))

if x > 100:
    raise TooHighValueError("The number is too high")

try: 1/x


except ZeroDivisionError:
    print("You can't divide by 0")

else:
    print("Well done")
finally:
    print("None")

# Exception raising
def test_func(x):
    if x > 100:
        raise TooHighValueError("The value of x is too high")
    assert(x>5), "The value is too low"

    if x == 69:
        raise FunnyNumberError(x, "The message is too funny")
    return None


test_x: int = int(input("plz give a number between 6 and 99"))
test_func(test_x)