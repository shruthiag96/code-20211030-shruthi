import pandas as pd
from src.bmi.utils.bmi_utils import *


class BmiCalculator:
    def __init__(self, args):
        self._data = pd.read_json(args.file)
        self._data = add_bmi(self._data, args.bmi_col, args.height_in_cm, args.weight_in_kg)
        conditions = get_conditions(self._data, args.bmi_col)
        self._data = add_bmi_category(self._data, args.category_col, conditions)
        self._data = add_health_risk(self._data, args.risk_col, conditions)

    def get_data(self):
        return self._data
