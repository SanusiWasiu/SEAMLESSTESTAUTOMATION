import sys
import os
sys.path.append(sys.path[0] + "/...")
sys.path.append(os.getcwd())
from Test.Scripts.test_login import TestLogin

if __name__ == "__main__":
    testObject = TestLogin()
    testObject.test_valid_login()
    testObject.test_invalid_login()