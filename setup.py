from setuptools import setup, find_packages

setup(
    name='bootcamp',
    version='0.1',
    packages=find_packages(),
    package_data={
        '': [
        ],
    },
    entry_points={
        'console_scripts': [
            'bootcamp=bootcamp.__main__:main'
        ]
    },
    test_suite='test',
    install_requires=[
        'behave',
    ],
    dependency_links=[],
)
