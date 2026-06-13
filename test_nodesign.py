# test_nodesign.py
"""
Tests for NodeSign module.
"""

import unittest
from nodesign import NodeSign

class TestNodeSign(unittest.TestCase):
    """Test cases for NodeSign class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeSign()
        self.assertIsInstance(instance, NodeSign)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeSign()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
