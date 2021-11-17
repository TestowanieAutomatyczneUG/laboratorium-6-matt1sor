import unittest
class Song:
    def __init__(self):
        self.lyrics = "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree." \
                      "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree." \
                      "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

    def showAll(self):
        res = [i + '.' for i in self.lyrics.split('.')]
        res.pop()
        return res

    def getVerse(self, num):
        if num > 12:
            raise ValueError("nie moze byc wiecej niz 12")
        elif num < 1:
            raise ValueError("nie moze byc mniej niz 1")
        else:
            return self.lyrics.split('.')[num - 1] + '.'

    def getVerses(self, num1, num2):
        if isinstance(num1, str) and isinstance(num2, int):
            raise ValueError("pierwszy parametr musi byc liczba")
        elif isinstance(num1, int) and isinstance(num2, str):
            raise ValueError("drugi paramter musi byc liczba")
        elif 1 <= num1 <= 12 and 1 <= num2 <= 12:
            return [self.lyrics.split('.')[i] + '.\n' for i in range(len(self.lyrics.split('.'))) if
                    (num1 - 1) <= i <= (num2 - 1)]
        else:
            raise ValueError("zle parametry")


class SongTest(unittest.TestCase):

    def test_show_all(self):
        self.assertEqual(self.song.showAll(), [
            'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.',
            'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
            'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.'
        ])

    def test_get_first_verse(self):
        self.assertEqual(self.song.getVerse(1), 'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')

    def test_get_second_verse(self):
        self.assertEqual(self.song.getVerse(2), 'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_get_third_verse(self):
        self.assertEqual(self.song.getVerse(3), 'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_get_fourth_verse(self):
        self.assertEqual(self.song.getVerse(4), 'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_get_fifth_verse(self):
        self.assertEqual(self.song.getVerse(5), 'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_get_sixth_verse(self):
        self.assertEqual(self.song.getVerse(6), 'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_get_seventh_verse(self):
        self.assertEqual(self.song.getVerse(7), 'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_get_eighth_verse(self):
        self.assertEqual(self.song.getVerse(8), 'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_get_ninth_verse(self):
        self.assertEqual(self.song.getVerse(9), 'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_get_tenth_verse(self):
        self.assertEqual(self.song.getVerse(10), 'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_get_eleventh_verse(self):
        self.assertEqual(self.song.getVerse(11), 'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_get_twelfth_verse(self):
        self.assertEqual(self.song.getVerse(12), 'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.')

    def test_get_verses_from_1_to_3(self):
        self.assertEqual(self.song.getVerses(1, 3), [
            'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n',
            'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n'
        ])

    def test_get_verses_from_4_to_8(self):
        self.assertEqual(self.song.getVerses(4, 8), [
            'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n',
            'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n'
        ])

    def test_get_verses_from_1_to_2(self):
        self.assertEqual(self.song.getVerses(1, 2), [
            'On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n',
            'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n'
        ])

    def test_get_verse_more_than_12(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.getVerse(13)

    def test_get_verse_less_than_1(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.getVerse(0)

    def test_get_verses_first_param_not_int(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.getVerses("", 3)

    def test_get_verses_second_param_not_int(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.getVerses(2, "3")


    def test_disallow_get_verses_first_param_less_than_1(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.getVerses(-1, 3)

    def test_disallow_get_verses_second_param_more_than_12(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.getVerses(11, 14)

    def test_disallow_get_verses_both_params_out_of_range(self):
        with self.assertRaisesWithMessage(ValueError):
            self.song.getVerses(44, 55)

    def setUp(self):
        self.song = Song()
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")