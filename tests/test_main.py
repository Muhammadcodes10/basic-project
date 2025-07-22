# 主程序测试
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.main import main
from src.utils import calculate_sum, format_message

def test_main():
    result = main()
    assert result == "Success"

def test_calculate_sum():
    assert calculate_sum(2, 3) == 5

def test_format_message():
    result = format_message("test")
    assert result == "[INFO] test"

if __name__ == "__main__":
    test_main()
    test_calculate_sum()
    test_format_message()
    print("All tests passed!")
