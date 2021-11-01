from unittest import TestCase
import pandas as pd
from pathlib import Path
from src.bmi.calculator.bmi import BmiCalculator
from src.bmi.utils.bmi_utils import *


class TestBmiCalculator(TestCase):
    def setUp(self):
        parser = create_parser()
        args = parser.parse_args(['--file', '../../../src/bmi/data.json', '--bmi_col', 'Bmi'])
        self.data = BmiCalculator(args).get_data()

    def is_calculator_data_valid(self):
        file_path = Path(__file__).parent.parent.parent.parent
        data = pd.read_json(file_path / 'src' / 'bmi' / 'bmi_data.json')
        self.assertEqual(self.data, data)




