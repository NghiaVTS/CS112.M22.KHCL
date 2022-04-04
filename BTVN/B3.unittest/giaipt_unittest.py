import unittest
import giaipt

class TestPT(unittest.TestCase):

    def test_giaipt(self):
        bien = (5,7)
        self.assertEqual(giaipt.giaipt(*bien), -7/5)

        bien = (0,0)
        self.assertEqual(giaipt.giaipt(*bien), "Phương trình có vô số nghiệm.")

        bien = (0,12)
        self.assertEqual(giaipt.giaipt(*bien), "Phương trình vô nghiệm.")
if __name__ == "__main__":
    unittest.main(verbosity = 2)
        