import unittest
from ranking import parseGameInput, calcScores, sortRankings

class TestRanking(unittest.TestCase):

    def test_parseGameInput(self):
        test_list = ['Wasps 3, Hornets 3']
        parsed_dict = parseGameInput(test_list)
        self.assertEqual(parsed_dict[0]['team1_name'], 'Wasps', 'Incorrecly parsed value: team1_name')
        self.assertEqual(parsed_dict[0]['team2_name'], 'Hornets', 'Incorrecly parsed value: team2_name')
        self.assertEqual(parsed_dict[0]['team1_score'], 3, 'Incorrecly parsed value: team1_score')
        self.assertEqual(parsed_dict[0]['team2_score'], 3, 'Incorrecly parsed value: team2_score')

    def test_calcScores(self):
        test_list = [
            {'team1_name': 'Wasps', 'team1_score': 3, 'team2_name': 'Hornets', 'team2_score': 3},
            {'team1_name': 'Wasps', 'team1_score': 2, 'team2_name': 'Hornets', 'team2_score': 1}
        ]
        scores = calcScores(test_list)
        self.assertEqual(scores['Wasps'], 4, 'Incorrect Score calculation')
        self.assertEqual(scores['Hornets'], 1, 'Incorrect Score calculation')

    def test_sortRankings(self):
        test_list = {'CC': 2, 'BB': 3, 'AA': 2}
        ranking = sortRankings(test_list)
        self.assertEqual(ranking[0][0], 'BB', 'Incorrect score order')
        self.assertEqual(ranking[1][0], 'AA', 'Incorrect score order')

if __name__ == '__main__':
    unittest.main()

