import unittest

from src.lab3.sudoku import group, get_row, get_col, find_empty_positions, get_block, find_possible_values, solve, check_solution, generate_sudoku


class SudokuTestCase(unittest.TestCase):

    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])
        self.assertEqual(group([9, 8, 7, 6, 5, 4, 3, 2, 1], 3), [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        self.assertEqual(group([12, 23, 34, 4, -9, 5, 8, 2], 4), [[12, 23, 34, 4], [-9, 5, 8, 2]])
        self.assertEqual(group([100, 10, 1000, 34, 0], 5), [[100, 10, 1000, 34, 0]])

    def test_get_row(self):
        self.assertEqual(get_row([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']], (1, 1)), ['.', '.', '.'])
        self.assertEqual(get_row([['2', '.', '8'], ['9', '.', '7'], ['.', '4', '.']], (2, 1)), ['.', '4', '.'])
        self.assertEqual(get_row([['.', '5', '.'], ['.', '6', '.'], ['.', '.', '.']], (1, 1)), ['.', '6', '.'])
        self.assertEqual(get_row([['1', '2', '3'], ['4', '5', '6'], ['9', '8', '7']], (0, 2)), ['1', '2', '3'])

    def test_get_col(self):
        self.assertEqual(get_col([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']], (1, 1)), ['.', '.', '.'])
        self.assertEqual(get_col([['2', '.', '.'], ['8', '1', '.'], ['.', '5', '7']], (0, 2)), ['.', '.', '7'])
        self.assertEqual(get_col([['.', '1', '9'], ['4', '2', '7'], ['.', '5', '.']], (0, 1)), ['1', '2', '5'])
        self.assertEqual(get_col([['.', '.', '.'], ['1', '5', '9'], ['2', '8', '4']], (2, 2)), ['.', '9', '4'])

    def test_get_block(self):
        grid = [
            ['.', '1', '.', '.', '.', '.', '.', '3', '.'],
            ['2', '.', '5', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '1', '.', '.'],
            ['9', '.', '6', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '4', '.'],
            ['.', '3', '.', '.', '5', '6', '7', '8', '9'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '5'],
            ['.', '.', '.', '.', '.', '.', '2', '.', '6']
        ]
        self.assertEqual(get_block(grid, (2, 1)), ['.', '1', '.', '2', '.', '5', '.', '.', '.'])
        self.assertEqual(get_block(grid, (8, 8)), ['7', '8', '9', '.', '.', '5', '2', '.', '6'])
        self.assertEqual(get_block(grid, (0, 7)), ['.', '3', '.', '.', '.', '.', '.', '.', '.'])
        self.assertEqual(get_block(grid, (6, 2)), ['.', '3', '.', '.', '.', '.', '.', '.', '.'])

    def test_find_empty_positions(self):
        self.assertEqual(find_empty_positions([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]), (0, 0))
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['.', '.', '.'], ['.', '.', '.']]), (1, 0))
        self.assertEqual(find_empty_positions([['6', '7', '2'], ['1', '8', '9'], ['3', '.', '.']]), (2, 1))
        self.assertEqual(find_empty_positions([['8', '.', '6'], ['.', '.', '.'], ['.', '.', '.']]), (0, 1))

    def test_find_possible_values(self):
        grid = [
            ['6', '1', '.', '.', '.', '7', '.', '3', '.'],
            ['2', '.', '5', '.', '4', '.', '.', '.', '.'],
            ['.', '.', '.', '2', '.', '.', '6', '.', '1'],
            ['.', '8', '.', '6', '.', '.', '1', '.', '.'],
            ['9', '7', '6', '.', '2', '.', '.', '.', '3'],
            ['.', '.', '1', '.', '.', '7', '.', '4', '.'],
            ['.', '3', '.', '.', '5', '6', '7', '8', '9'],
            ['.', '.', '.', '.', '.', '.', '.', '.', '5'],
            ['5', '.', '4', '.', '1', '.', '2', '.', '6']
        ]
        self.assertEqual(find_possible_values(grid, (0, 2)), {'8', '9'})
        self.assertEqual(find_possible_values(grid, (7, 3)), {'3', '4', '7', '8', '9'})
        self.assertEqual(find_possible_values(grid, (5, 8)), {'2', '8'})
        self.assertEqual(find_possible_values(grid, (0, 8)), {'2', '4', '8'})

    def test_solve(self):
        grid = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        expected_solution = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
        self.assertEqual(solve(grid), expected_solution)

    def test_check_solution(self):
        solution1 = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
        self.assertEqual(check_solution(solution1), True)
        solution2 = [
            ["5", "3", "4", "6", "7", "8", "9", "1", "8"],
            ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
            ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
            ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
            ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
            ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
            ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
            ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
            ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
        ]
        self.assertEqual(check_solution(solution2), False)

    def test_generate_sudoku(self):
        grid = generate_sudoku(40)
        num_filled = sum(1 for row in grid for e in row if e != ".")
        self.assertEqual(num_filled, 40)
        solution = solve(grid)
        self.assertEqual(check_solution(solution), True)

        grid = generate_sudoku(0)
        num_filled = sum(1 for row in grid for e in row if e != ".")
        self.assertEqual(num_filled, 0)
        solution = solve(grid)
        self.assertEqual(check_solution(solution), True)

        grid = generate_sudoku(81)
        num_filled = sum(1 for row in grid for e in row if e != ".")
        self.assertEqual(num_filled, 81)
        solution = solve(grid)
        self.assertEqual(check_solution(solution), True)

        grid = generate_sudoku(1000)
        num_filled = sum(1 for row in grid for e in row if e != ".")
        self.assertEqual(num_filled, 81)
        solution = solve(grid)
        self.assertEqual(check_solution(solution), True)
