
from setuptools import setup, find_packages

setup(
    name='TSFEDL',
    version='1.0.0',
    description='Hybrid deep learning models for time series forecasting',
    author='José Manuel Infante',
    author_email='tu.correo@ejemplo.com',
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'numpy',
        'scikit-learn',
        'matplotlib',
    ],
)
