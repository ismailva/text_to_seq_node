import unittest
import sys
import os
root_dir = os.path.abspath(os.path.dirname(__file__))


# Discover and run all tests in the 'test' directory
loader = unittest.TestLoader()
suite = loader.discover(start_dir='test', pattern='test_*.py', top_level_dir=root_dir)

runner = unittest.TextTestRunner()
runner.run(suite)

# this can be also done in terminal by running below command
# python3 -m unittest discover -s test