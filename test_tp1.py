import unittest

from module_runner import ModuleRunner

class TestExercice1(unittest.TestCase): 
    def setUp(self) -> None:
        self.maxDiff = None
        self.runner = ModuleRunner('ex1')
        self.input_questions = "De quelle nationalité est l'athlète ? Quel est son nom ? Date du record ? Dans quelle discipline ? Dans une catégorie spécifique ? Quel est le record ? "
        return super().setUp()
    
    def format_tests(self, country: str, athlete: str, date: str, sport: str, category: str, record: str):
        simulated_inputs = f"{country}\n{athlete}\n{date}\n{sport}\n{category}\n{record}\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}\nNouveau Record:\n--------------------\n{date} - {sport} - {category}:\n\t{athlete} ({country}) - {record}\n"
        self.assertEqual(expected, output)

    def test_exercice1_swimmer(self):
        country = "CAN"
        athlete = "Summer McIntosh"
        date = "1/8/2024"
        sport = "Natation"
        category = "200M Papillon"
        record = "2:3.03"
        self.format_tests(country, athlete, date, sport, category, record)

    def test_exercice1_pole_vault(self):
        country = "SW"
        athlete = "Armand Duplantis"
        date = "25/8/2024"
        sport = "Athlétisme"
        category = "Saut à la perche"
        record = "6.25m"
        self.format_tests(country, athlete, date, sport, category, record)

class TestExercice2(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.runner = ModuleRunner('ex2')
        self.input_questions = "Quelle quantité d'eau faut-il assainir ? "
        return super().setUp()

    def format_tests(self, water_quantity: float, n_filter: int, n_light: int, kg_chlorine: float):
        simulated_inputs = f"{water_quantity}\n"
        output = self.runner.run(simulated_inputs)
        expected = f"""{self.input_questions}Voici les éléments requis pour assainir {water_quantity}L d'eau:
\t- Filtre(s) : {n_filter}
\t- Lampe(s) UV : {n_light}
\t- Chlore : {kg_chlorine}kg\n"""
        self.assertEqual(expected, output)

    def test_standard_water(self):
        water_quantity = 5.0
        expected_filter = 1
        expected_light = 3
        expected_chlorine = 0.5
        self.format_tests(water_quantity, expected_filter, expected_light, expected_chlorine)

    def test_standard_water_float(self):
        water_quantity = 35.0
        expected_filter = 7
        expected_light = 21
        expected_chlorine = 3.5
        self.format_tests(water_quantity, expected_filter, expected_light, expected_chlorine)

class TestExercice3(unittest.TestCase): 
    def setUp(self) -> None: 
        self.maxDiff = None
        self.runner = ModuleRunner('ex3')
        self.input_questions = "Vitesse initiale (m/s): Angle de lancer (en degrés): "

    def test_standard_speed(self): 
        speed = 20.5
        angle = 30
        distance = 37.14
        simulated_inputs = f"{speed}\n{angle}\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Distance parcourue: {distance}m\n"
        self.assertEqual(output, expected)

    def test_standard_speed2(self): 
        speed = 45
        angle = 2
        distance = 14.41
        simulated_inputs = f"{speed}\n{angle}\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Distance parcourue: {distance}m\n"
        self.assertEqual(output, expected)

class TestExercice4(unittest.TestCase): 
    def setUp(self) -> None:
        self.maxDiff = None
        self.runner = ModuleRunner('ex4')
        self.input_questions = "Pourcentage de batterie ? "

    def test_empty_battery(self): 
        battery_percentage = 0
        simulated_inputs = f"{battery_percentage}\n"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}La batterie est vide\n"
        self.assertEqual(output, expected)

    def test_twelve_percents(self): 
        battery_percentage = 12
        simulated_inputs = f"{battery_percentage}\n"
        distance = 44.5
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}{distance} km\n"
        self.assertEqual(output, expected)


    def test_twenty_two(self): 
        battery_percentage = 22.5
        simulated_inputs = f"{battery_percentage}\n"
        distance = 55.0
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}{distance} km\n"
        self.assertEqual(output, expected)


    def test_seventy_four(self): 
        battery_percentage = 74
        simulated_inputs = f"{battery_percentage}\n"
        distance = 118.0
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}{distance} km\n"
        self.assertEqual(output, expected)


    def test_forty_nine(self): 
        battery_percentage = 49
        simulated_inputs = f"{battery_percentage}\n"
        distance = 69.5
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}{distance} km\n"
        self.assertEqual(output, expected)

class TestExercice5(unittest.TestCase): 
    def setUp(self) -> None:
        self.maxDiff = None
        self.runner = ModuleRunner('ex5')
        self.input_questions = "Pays concerné ? Chaine représentant les médailles ? "
        return super().setUp()

    def test_standard_medals(self): 
        country = "France"
        medals = "GSBS"
        simulated_inputs = f"{country}\n{medals}"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}{country}:\n- 1 Or\n- 2 Argent\n- 1 Bronze\n"
        self.assertEqual(output, expected)


    def test_standard_medals2(self): 
        country = "CAN"
        medals = "GSBSSGBSGSSGBSBBBGGSSSS"
        simulated_inputs = f"{country}\n{medals}"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}{country}:\n- 6 Or\n- 11 Argent\n- 6 Bronze\n"
        self.assertEqual(output, expected)
    
    def test_wrong_str(self):
        country = "CAN"
        medals = "A"
        simulated_inputs = f"{country}\n{medals}"
        output = self.runner.run(simulated_inputs)
        expected = f"{self.input_questions}Ceci est une chaine invalide.\n"
        self.assertEqual(output, expected)

if __name__ == "__main__": 
    unittest.main()