import unittest

class Roman:
    def __init__(self):
        self.nums = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

    def roman(self, value):
        result = ""
        for val, num in sorted(self.nums.items(), reverse=True):
            while value >= val:
                result += num
                value -= val
        return result


class RomanNumeralsTest(unittest.TestCase):
    def test_1_is_a_single_i(self):
        self.assertEqual(self.temp.roman(1), "I")

    def test_2_is_two_i_s(self):
        self.assertEqual(self.temp.roman(2), "II")

    def test_3_is_three_i_s(self):
        self.assertEqual(self.temp.roman(3), "III")

    def test_4_being_5_1_is_iv(self):
        self.assertEqual(self.temp.roman(4), "IV")

    def test_5_is_a_single_v(self):
        self.assertEqual(self.temp.roman(5), "V")

    def test_6_being_5_1_is_vi(self):
        self.assertEqual(self.temp.roman(6), "VI")

    def test_9_being_10_1_is_ix(self):
        self.assertEqual(self.temp.roman(9), "IX")

    def test_20_is_two_x_s(self):
        self.assertEqual(self.temp.roman(27), "XXVII")

    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(self.temp.roman(48), "XLVIII")

    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(self.temp.roman(49), "XLIX")

    def test_50_is_a_single_l(self):
        self.assertEqual(self.temp.roman(59), "LIX")

    def test_90_being_100_10_is_xc(self):
        self.assertEqual(self.temp.roman(93), "XCIII")

    def test_100_is_a_single_c(self):
        self.assertEqual(self.temp.roman(141), "CXLI")

    def test_60_being_50_10_is_lx(self):
        self.assertEqual(self.temp.roman(163), "CLXIII")

    def test_400_being_500_100_is_cd(self):
        self.assertEqual(self.temp.roman(402), "CDII")

    def test_500_is_a_single_d(self):
        self.assertEqual(self.temp.roman(575), "DLXXV")

    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(self.temp.roman(911), "CMXI")

    def test_1000_is_a_single_m(self):
        self.assertEqual(self.temp.roman(1024), "MXXIV")

    def test_3000_is_three_m_s(self):
        self.assertEqual(self.temp.roman(3000), "MMM")
    def setUp(self):
        self.temp =Roman()