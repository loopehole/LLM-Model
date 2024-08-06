from setuptools import setup, find_packages

setup(
    name='llm_project',
    version='1.0.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'torch',
        'transformers',
        'scikit-learn',
    ],
    test_suite='tests',
)
