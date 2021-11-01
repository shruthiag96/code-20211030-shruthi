from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='bmi-calculator',
    version='0.0.1',
    description='Project to calculate bmi given data with height and weight',
    install_requires=requirements
)