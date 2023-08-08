import pytest


def identity(x):
    return x 

def test_main():
    assert identity(3) == 3

if __name__ == '__main__':
    test_main()