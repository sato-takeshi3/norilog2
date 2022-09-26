from setuptools import setup
setup(name='norilog')

from setuptools import setup, find_packages

setup(
    name='norilog',
    varsion='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        ],
    entry_points="""
        [console_scripts]
        norilog = norilog:main
    """,
    )

