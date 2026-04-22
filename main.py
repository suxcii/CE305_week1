from q1_base_conversion import base_conv
from q2_floating_model import floating_model


from datetime import datetime
def show_time():
    print(datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y"))



def run_q1_tests():
    print("\n=== Question 1: Base Conversion ===")
    show_time()
    tests = [
        ("123-45-6", 44, 23),
        ("123-45-6", 46, 23),
        ("6-54-3-21-", 46, 23),
        ("6-54-3-21-", 63, 74),
        ("-12-9-45-6", 46, 70),

    ]

    for i, (num, base, new_base) in enumerate(tests, 1):
        print(f"\nTest {i}")
        show_time()
        print(f"Input : base_conv({num!r}, {base}, {new_base})")
        print("Output:")
        print(base_conv(num, base, new_base))


def run_q2_test():
    print("\n=== Question 2: 14-bit Floating Model ===")
    show_time()
    print("Input : floating_model(-26.625)")
    print("Output:")
    print(floating_model(-26.625))


if __name__ == "__main__":
    
    run_q1_tests()
    
    run_q2_test()