from unittest import TestCase
import isaacpost1424


class TestRename(TestCase):
    def test_rename1_essential(self): # Test expected input.
        testString = "Some Flavor - The Binding of Isaac - AFTERBIRTH+ - Northernlion Plays - Episode 5000"
        expectedString = "The Binding of Isaac - AFTERBIRTH+ - Northernlion Plays - Episode 5000 [Some Flavor]"

        (_, result) = isaacpost1424.rename(testString)

        self.assertEqual(result, expectedString)

    def test_rename2_essential(self):  # Test variation of expected input.
        testString = "Some Flavor - The Binding of Isaac: AFTERBIRTH+ - Northernlion Plays - Episode 5000"
        expectedString = "The Binding of Isaac: AFTERBIRTH+ - Northernlion Plays - Episode 5000 [Some Flavor]"

        (_, result) = isaacpost1424.rename(testString)

        self.assertEqual(result, expectedString)

    def test_rename3(self):  # Test unexpected, but similar input.
        testString = "Some Flavor - The Bining of Isac: AFTERBIRT+ - Nothenlion Play - Episode 5000"

        self.assertEqual(isaacpost1424.rename(testString)[1], None)

    def test_rename4(self):  # Test unexpected input.
        testString = "something really wrong"

        self.assertEqual(isaacpost1424.rename(testString)[1], None)

    def test_rename5(self):  # Test wrong type.
        testInput = 23

        self.assertRaises(Exception, isaacpost1424.rename, testInput)
