import unittest
from foobar import get_foobar_output


class TestFooBar(unittest.TestCase):

    def test_divisible_by_three(self):
        """Test numeri divisibili per 3"""
        print("Test 1: Controllo numeri divisibili per 3")
        try:
            self.assertEqual(get_foobar_output(3), "Foo")
            self.assertEqual(get_foobar_output(6), "Foo")
            self.assertEqual(get_foobar_output(9), "Foo")
            print("OK! ✅")
        except AssertionError:
            print("❌ Test fallito: i numeri divisibili per 3 devono restituire 'Foo'")
            raise

    def test_divisible_by_five(self):
        """Test numeri divisibili per 5"""
        print("Test 2: Controllo numeri divisibili per 5")
        try:
            self.assertEqual(get_foobar_output(5), "Bar")
            self.assertEqual(get_foobar_output(10), "Bar")
            self.assertEqual(get_foobar_output(20), "Bar")
            print("OK! ✅")
        except AssertionError:
            print("❌ Test fallito: i numeri divisibili per 5 devono restituire 'Bar'")
            raise

    def test_divisible_by_three_and_five(self):
        """Test numeri divisibili per 3 e 5"""
        print("Test 3: Controllo numeri divisibili sia per 3 che per 5")
        try:
            self.assertEqual(get_foobar_output(15), "FooBar")
            self.assertEqual(get_foobar_output(30), "FooBar")
            self.assertEqual(get_foobar_output(45), "FooBar")
            print("OK! ✅")
        except AssertionError:
            print("❌ Test fallito: i numeri divisibili per 3 e 5 devono restituire 'FooBar'")
            raise

    def test_not_divisible(self):
        """Test numeri non divisibili"""
        print("Test 4: Controllo numeri non divisibili né per 3 né per 5")
        try:
            self.assertEqual(get_foobar_output(1), "1")
            self.assertEqual(get_foobar_output(2), "2")
            self.assertEqual(get_foobar_output(7), "7")
            print("OK! ✅")
        except AssertionError:
            print("❌ Test fallito: i numeri non divisibili devono restituire il numero stesso")
            raise

    def tearDown(self):
        print("----------------------------------------------------------------------")


if __name__ == "__main__":
    print("\n=== Test FooBar ===")
    unittest.main(verbosity=1)
