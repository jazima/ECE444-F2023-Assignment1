from utils import utils

int_test_inputs = [1145, 44531, 33466, 833846, 8376, 888835, 833776, 200030, 8876, 611554,
                   299509, 77374]
int_test_reversed_outputs = [5411, 13544, 66433, 648338, 6738, 538888, 677338, 30002, 6788, 455116,
                             905992, 47377]
int_test_formatter_outputs = [(bin(i), oct(i)) for i in int_test_inputs]

# Reversed Test
print("Testing utils.reversed with integer inputs")
for index, input in enumerate(int_test_inputs):
    try:
        assert(utils.reversed(input) == int_test_reversed_outputs[index])
    except AssertionError:
        print(f"Invalid output for input: {input}. Expected ({int_test_reversed_outputs[index]}). Got ({utils.reversed(input)})")
    except TypeError:
        print(f"Invalid input type for input: {input}")
print("\n\n")

print("Testing utils.reversed with string input")
try:
    utils.reversed("1445")
    print(f"Expected TypeError but no Error was raised for input ({input}), output ({utils.reversed('1445')})")
except TypeError:
    pass
except Exception as ex:
    print(f"Unexpected exception raised ({ex})")
print("\n\n")

print("Testing utils.reversed with float input")
try:
    utils.reversed(1445.0)
    print(f"Expected TypeError but no Error was raised for input ({input}), output ({utils.reversed(1445.0)})")
except TypeError:
    pass
except Exception as ex:
    print(f"Unexpected exception raised ({ex})")
print("\n\n")

# Formatter Test
print("Testing utils.formatter with integer inputs")
for index, input in enumerate(int_test_inputs):
    try:
        assert(utils.formatter(input) == int_test_formatter_outputs[index])
    except AssertionError:
        print(f"Invalid output for input: {input}. Expected ({int_test_formatter_outputs[index]}). Got ({utils.formatter(input)})")
    except TypeError:
        print(f"Invalid input type for input: {input}")
print("\n\n")

print("Testing utils.formatter with string input")
try:
    utils.formatter("1445")
    print(f"Expected TypeError but no Error was raised for input ('1445'), output ({utils.formatter('1445')})")
except TypeError:
    pass
except Exception as ex:
    print(f"Unexpected exception raised ({ex})")
print("\n\n")

print("Testing utils.formatter with float input")
try:
    utils.formatter(1445.0)
    print(f"Expected TypeError but no Error was raised for input ({input}), output ({utils.formatter(1445.0)})")
except TypeError:
    pass
except Exception as ex:
    print(f"Unexpected exception raised ({ex})")