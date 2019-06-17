#!/bin/env python
import pdb
import unittest

# Meta-tests on the acquisition of the code to be tested
# Can it be imported and tested?
class TestMetaMethods(unittest.TestCase):
	def test_import(self):
		self.assertTrue(False)
	
# Tests on the nodes' existance and arguments, 
# interfacing with them through getters and setters
# and provide a wide berth on the kinds of argument objects
# they hold.

# Tests on node linkages and groupings
# They must match along the whole node tree

# Tests on node processing in paths:
# prerequirements, path lengths...

# Run the tests
if __name__ == "__main__":
	unittest.main()
