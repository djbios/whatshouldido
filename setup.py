from setuptools import setup

setup(
    name='whattodo',
    version='0.1.0',
    py_modules=['whattodo'],
    install_requires=[
        'Click',
        'termcolor',
        'GitPython',
        'tabulate'
    ],
    entry_points={
        'console_scripts': [
            'whattodo = whattodo:list_todos',
        ],
    },
)