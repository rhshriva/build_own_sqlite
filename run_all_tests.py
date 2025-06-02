import unittest

if __name__ == "__main__":
    # Discover all tests in the 'tests' directory
    loader = unittest.TestLoader()
    suite = loader.discover('tests')

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite) 