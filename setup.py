from setuptools import setup, find_packages

setup(
    name='diabete',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'trainDiabete = diabete.trainDiabete:main',
            'inferenceDiabete = diabete.inferenceDiabete:main',
        ],
    },

)
