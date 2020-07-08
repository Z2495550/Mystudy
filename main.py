import pytest
import allure
import os

if __name__ == '__main__':
    args = ['-s','-q']
    pytest.main(args)
    # os.system('allure generate report/xml -o report/html')
