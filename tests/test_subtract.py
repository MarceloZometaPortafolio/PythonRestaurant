import pytest
from lib.subtract import subtract

class Test_Subtract:

    def test_sub(self):
        assert subtract(2,2) == 0