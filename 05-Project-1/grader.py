import subprocess
import platform
import pathlib
import random
import sys


low_customer_output = "Your tip options are:\n15%: ${}\n20%: ${}\n25%: ${}"
high_customer_output = "A 20% tip is automatically added to parties of 8 or more. Your bill is ${}."

grader_root = str(pathlib.Path(__file__).parent.resolve())
exe_file = grader_root + "/calculator.py"

py_exe = "py3" if platform.system == "Windows" else "python3"

def make_expected_output(expected):
    message = low_customer_output
    if expected["auto_tip"]:
        message = high_customer_output
    return message.format(*expected["tips"])

def test_case(bill, customers):
    tips = [round(bill * 1.2, 2)]
    if customers < 8:
        tips.insert(0, round(bill * 1.15, 2))
        tips.append(round(bill * 1.25, 2))
        
    return {
        "bill": bill,
        "customers": customers,
        "expected": {
            "auto_tip": customers >= 8,
            "tips": tips    
        }
    }

def random_case():
    bill = random.uniform(0, 1000)
    customers = random.randint(1, 100)
    return test_case(bill, customers)

test_cases = [
    test_case(100, 2),
    test_case(100, 8),
    test_case(30.64, 5),
    test_case(87.388, 12)
]    

def run_test(test_case, print_success = True):
    test_input = str(case["bill"]) + "\n" + str(case["customers"])
    try:
        results = subprocess.run([py_exe, exe_file], 
                                input = test_input,
                                capture_output = True, 
                                text = True,
                                check = True)
        results.check_returncode()
        output = results.stdout.strip()

        expected = make_expected_output(case["expected"])

        if output != expected:
            print("({}, {}) \033[31mFail\033[39m".format(case["bill"], case["customers"]))
            print("Expected: " + expected)
            print("Got     : " + output)
            return False
        else:
            if print_success:
                print("({}, {}) \033[92mPass\033[39m".format(case["bill"], case["customers"]))
            return True

    except subprocess.CalledProcessError as e:
        print("Test case ({}, {}) exitted unexpectedly.".format(case["bill"], case["customers"]))
        if(e.stderr != None and len(e.stderr) > 0):
            print("Error message: ")
            print(e.stderr)
        return False


for case in test_cases:
    run_test(case)

if "-r" in sys.argv or "--random" in sys.argv:
    test_amount = 1000
    print("Running random tests")
    for i in range(test_amount):
        case = random_case()
        if not run_test(case, print_success = False):
            print("\033[31mRandom test ({}, {}) failed. Terminating.\033[39m".format(case["bill"], case["customers"]))
            break
        print("Progress: {}%\r".format(i / (test_amount / 100)), end = "")
    else:
        print("\033[92mSuccess! {} random tests passed!\033[39m".format(test_amount))

