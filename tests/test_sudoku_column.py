#!/usr/bin/env python3

import unittest

from src.sudoku_column import column_correct


SUDOKU = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2],
]

# A second grid where several columns have been mutated to contain a
# repeated nonzero digit, used to exercise both the True and False paths.
CHECK_SUDOKU = [
    [9, 0, 1, 0, 8, 0, 3, 0, 1],
    [2, 2, 0, 0, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 4, 0, 4],
    [2, 9, 4, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 8, 6],
    [3, 0, 1, 0, 0, 0, 0, 0, 1],
    [3, 0, 0, 0, 2, 0, 2, 0, 1],
]


def column(sudoku, index):
    return [row[index] for row in sudoku]


class TestColumnCorrect(unittest.TestCase):

    def test_worked_example(self):
        result = column_correct(SUDOKU, 0)
        self.assertEqual(
            result, True,
            msg="column_correct(sudoku, 0) should be True for column 0 = "
                "%s: no nonzero digit is repeated (zeros are blanks and "
                "don't count)." % (column(SUDOKU, 0),))

    def test_return_type_is_bool(self):
        result = column_correct(SUDOKU, 0)
        self.assertIsInstance(
            result, bool,
            msg="column_correct(sudoku, 0) should return a bool, not %s. "
                "Got %r." % (type(result).__name__, result))

    def test_valid_columns(self):
        for col in [3, 4, 7]:
            with self.subTest(column=col):
                result = column_correct(CHECK_SUDOKU, col)
                self.assertEqual(
                    result, True,
                    msg="column_correct(sudoku, %d) should be True for "
                        "column %s: no nonzero digit is repeated."
                        % (col, column(CHECK_SUDOKU, col)))

    def test_invalid_columns(self):
        for col in [0, 1, 2, 6, 8]:
            with self.subTest(column=col):
                result = column_correct(CHECK_SUDOKU, col)
                self.assertEqual(
                    result, False,
                    msg="column_correct(sudoku, %d) should be False for "
                        "column %s: a nonzero digit is repeated."
                        % (col, column(CHECK_SUDOKU, col)))

    def test_column_of_all_zeros_is_valid(self):
        blank_sudoku = [[0] * 9 for _ in range(9)]
        result = column_correct(blank_sudoku, 4)
        self.assertEqual(
            result, True,
            msg="column_correct(sudoku, 4) should be True when column 4 is "
                "all zeros: an empty column has no repeated nonzero digit.")


if __name__ == "__main__":
    unittest.main()
