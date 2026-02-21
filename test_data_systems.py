import unittest
from data_systems import (
    MIN_INT32, MAX_INT32,
    detect_overflow_and_saturate,
    dec_to_bin32_twos_complement,
    bin32_to_hex8,
    bin32_to_signed_decimal,
    convert_invocation,
)


class TestDataSystems(unittest.TestCase):

    def test_positive(self):
        r = convert_invocation("123", "HEX")
        self.assertEqual(r["value_out"], "0x0000007B")
        self.assertEqual(r["overflow"], 0)
        self.assertEqual(r["saturated"], 0)

    def test_zero(self):
        r = convert_invocation("0", "BIN")
        self.assertEqual(r["value_out"], "0"*32)

    def test_negative(self):
        r = convert_invocation("-123", "HEX")
        self.assertEqual(r["value_out"], "0xFFFFFF85")

    def test_boundaries(self):
        self.assertEqual(convert_invocation(str(MAX_INT32), "DEC")["value_out"], str(MAX_INT32))
        self.assertEqual(convert_invocation(str(MIN_INT32), "DEC")["value_out"], str(MIN_INT32))

    def test_overflow(self):
        r = convert_invocation(str(MAX_INT32+1), "DEC")
        self.assertEqual(r["overflow"], 1)
        self.assertEqual(r["saturated"], 1)


if __name__ == "__main__":
    unittest.main()
