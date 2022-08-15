import pytest
import unittest
import scripts.playground as pg


class TestPlayground(unittest.TestCase):

    def test_fibonacci_with_simple_test(self):
         fib = pg.fibonacci(1,2,5)
         expected_output = [1,2,3,5]
         assert fib == expected_output