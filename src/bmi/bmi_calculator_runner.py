from src.bmi.calculator.bmi import BmiCalculator
from src.bmi.utils.bmi_utils import *


class BmiCalcRunner:
    def __init__(self, args):
        calculator = BmiCalculator(args)
        data = calculator.get_data()
        overweight = get_filtered_by_col_count(data, args.category_col, 'Overweight')
        print(f"No of Overweight people in the given dataset is {overweight}")


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    BmiCalcRunner(args)
