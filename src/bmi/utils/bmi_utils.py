import argparse
import logging
import numpy as np

logging.basicConfig(filename='../../calculator.log', level=logging.DEBUG)

DEFAULT_CATEGORY_CHOICES = ['Underweight', 'Normal weight', 'Overweight', 'Moderately obese', 'Severely obese',
                   'Very severely obese']
DEFAULT_RISK_CHOICES = ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk', 'High risk', 'Very high risk']


def create_parser():
    parser = argparse.ArgumentParser('Arguments parser for BMI calculate runner')
    parser.add_argument('--file', dest='file',
                        help='Absolute file path with raw data', default='data.json')
    parser.add_argument('--bmi_col', dest='bmi_col',
                        help='Absolute file path with raw data', default='Bmi')
    parser.add_argument('--height_in_cm', dest='height_in_cm',
                        help='Absolute file path with raw data', default='HeightCm')
    parser.add_argument('--weight_in_kg', dest='weight_in_kg',
                        help='Absolute file path with raw data', default='WeightKg')
    parser.add_argument('--cat_col', dest='category_col',
                        help='Absolute file path with raw data', default='BmiCategory')
    parser.add_argument('--risk_col', dest='risk_col',
                        help='Absolute file path with raw data', default='HealthRisk')
    return parser


def add_bmi(data, bmi_col, height_in_cm_col, weight_in_kg_col):
    cols = data.columns
    if weight_in_kg_col in cols and weight_in_kg_col in cols:
        data[bmi_col] = data[weight_in_kg_col] * pow(10, 4) / pow(data[height_in_cm_col], 2)
        return round(data, 1)
    else:
        raise Exception(f'Column/s {weight_in_kg_col, weight_in_kg_col} is/are not found')


def get_conditions(data, bmi_col):
    if bmi_col not in data.columns:
        raise Exception(f'Column {bmi_col} is not found')
    return [(data[bmi_col] <= 18.4),
            (data[bmi_col] >= 18.5) & (data[bmi_col] <= 24.9),
            (data[bmi_col] >= 25) & (data[bmi_col] <= 29.9),
            (data[bmi_col] >= 30) & (data[bmi_col] <= 34.9),
            (data[bmi_col] >= 35) & (data[bmi_col] <= 39.9),
            (data[bmi_col] >= 40)]


def add_col_by_conditions(data, col, conditions, choices):
    if len(choices) != len(conditions):
        raise Exception(f'Conditions length not matching with choices provided {choices}')
    data[col] = np.select(conditions, choices)
    return data


def add_bmi_category(data, category_col, conditions, choices=DEFAULT_CATEGORY_CHOICES):
    return add_col_by_conditions(data, category_col, conditions, choices)


def add_health_risk(data, risk_col, conditions, choices=DEFAULT_RISK_CHOICES):
    return add_col_by_conditions(data, risk_col, conditions, choices)


def get_filtered_by_col_count(data, col, value):
    if col in data.columns:
        count = data[data[col] == value][col].count()
        if not count:
            return 0
        return count
    else:
        raise Exception('Could not find column BmiCategory')


