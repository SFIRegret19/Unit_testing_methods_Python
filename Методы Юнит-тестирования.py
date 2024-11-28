import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += (self.speed * 2)

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.all_results = {}

    @classmethod
    def tearDownClass(self):
        for results in self.all_results.values():
            res = {key: str(value) for key, value in results.items()}
            print(res)

    def setUp(self):
        self.Usein = Runner('Усэйн', 10)
        self.Andrew = Runner('Андрей', 9)
        self.Nik = Runner('Ник', 3)

    def test_Usein_Nik(self):
        tournament = Tournament(90, self.Usein, self.Nik)
        finishers = tournament.start()
        self.all_results['test_Usein_Nik'] = finishers
        self.assertEqual(str(finishers[max(finishers.keys())]), 'Ник')

    def test_Andrew_Nik(self):
        tournament = Tournament(90, self.Andrew, self.Nik)
        finishers = tournament.start()
        self.all_results['test_Andrew_Nik'] = finishers
        self.assertEqual(str(finishers[max(finishers.keys())]), 'Ник')

    def test_Usein_Andrew_Nik(self):
        tournament = Tournament(90, self.Usein, self.Andrew, self.Nik)
        finishers = tournament.start()
        self.all_results['test_Usein_Andrew_Nik'] = finishers
        self.assertEqual(str(finishers[max(finishers.keys())]), 'Ник')


if __name__ == "__main__":
    unittest.main()