from unittest import TestCase
import nlmtrain


testingScript = nlmtrain

class TestRename(TestCase):
    def test_rename1_essential(self): # Test expected input.
        testString = "Some Flavor _ Monster Train (Episode 5000)"
        expectedString = "Monster Train - Episode 5000 - Some Flavor"

        (_, result) = testingScript.rename(testString)

        self.assertEqual(result, expectedString)

    # def test_rename2_essential(self):  # Test variation of expected input.
    #     testString = ""
    #     expectedString = ""
    #
    #     (_, result) = testingScript.rename(testString)
    #
    #     self.assertEqual(result, expectedString)

    def test_rename3(self):  # Test unexpected, but similar input.
        testString = "Some Flavor _ not really mtrain - Episode 5000"

        self.assertEqual(testingScript.rename(testString)[1], None)

    def test_rename4(self):  # Test unexpected input.
        testString = "bad input"

        self.assertEqual(testingScript.rename(testString)[1], None)

    def test_rename5(self):  # Test wrong type.
        testInput = 23

        self.assertRaises(Exception, testingScript.rename, testInput)
