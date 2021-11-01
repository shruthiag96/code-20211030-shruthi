from unittest import TestCase
import pandas as pd
from pathlib import Path
from src.bmi.utils.bmi_utils import *


class TestBmiUtils(TestCase):

    def setUp(self):
        file_path = Path(__file__).parent.parent.parent.parent
        self.raw_data = pd.read_json(file_path / 'src' / 'bmi' / 'data.json')
        self.bmi_data = pd.read_json(file_path / 'src' / 'bmi' / 'bmi_data.json')

    def test_add_bmi(self):
        data = add_bmi(self.raw_data, 'Bmi', 'HeightCm', 'WeightKg')
        expected = [32.8, 32.8, 23.8, 22.5, 31.1, 29.4]
        self.assertEqual(data['Bmi'].values.tolist(), expected)

    def test_add_bmi__when_no_columns_found(self):
        with self.assertRaises(Exception):
            add_bmi(self.raw_data, 'Bmi', 'Height', 'Weight')

    def test_get_conditions_with_no_bmi_col(self):
        data = add_bmi(self.raw_data, 'Bmi', 'HeightCm', 'WeightKg')
        with self.assertRaises(Exception):
            get_conditions(data, 'invalid_col')

    def test_add_bmi_category(self):
        bmi_col = 'Bmi'
        data = self.bmi_data
        conditions = get_conditions(data, bmi_col)
        category_col = 'BmiCategory'
        data = add_bmi_category(data, category_col, conditions)
        expected = ['Moderately obese', 'Moderately obese', 'Normal weight', 'Normal weight', 'Moderately obese', 'Overweight']
        self.assertEqual(data[category_col].values.tolist(), expected)

    def test_add_bmi_category_with_unmatching_choices(self):
        bmi_col = 'Bmi'
        data = self.bmi_data
        conditions = get_conditions(data, bmi_col)
        category_col = 'BmiCategory'
        with self.assertRaises(Exception):
            add_bmi_category(data, category_col, conditions, ['Underweight', 'Normal weight', 'Overweight'])

    def test_add_health_risk(self):
        bmi_col = 'Bmi'
        data = self.bmi_data
        conditions = get_conditions(data, bmi_col)
        category_col = 'HealthRisk'
        data = add_health_risk(data, category_col, conditions)
        expected = ['Medium risk', 'Medium risk', 'Low risk', 'Low risk', 'Medium risk', 'Enhanced risk']
        self.assertEqual(data[category_col].values.tolist(), expected)

    def test_add_health_risk_with_unmatching_choices(self):
        bmi_col = 'Bmi'
        data = self.bmi_data
        conditions = get_conditions(data, bmi_col)
        category_col = 'HealthRisk'
        with self.assertRaises(Exception):
            add_bmi_category(data, category_col, conditions, ['Malnutrition risk', 'Low risk'])

    def test_get_filtered_by_col_count(self):
        count_of_moderately_obese_people = get_filtered_by_col_count(self.bmi_data, 'BmiCategory', 'Moderately obese')
        self.assertEqual(count_of_moderately_obese_people, 3)

        count_of_people_with_low_risk = get_filtered_by_col_count(self.bmi_data, 'HealthRisk', 'Low risk')
        self.assertEqual(count_of_people_with_low_risk, 2)

    def test_get_filtered_by_col_count_with_unknown_col(self):
        with self.assertRaises(Exception):
            get_filtered_by_col_count(self.bmi_data, 'Invalid', 'Moderately obese')



