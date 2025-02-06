from setuptools import setup, find_packages

setup(
    name='textSummarizer',
    version='1.0.0',
    description='A text summarizer project',
    author='my Name',
    author_email='mail@email.com',
    packages=find_packages(),
    install_requires=[
        'nltk',
        'numpy==1.26.4',
        'torch==2.5',
    ],
    entry_points={
        'console_scripts': [
            'text-summarizer = text_summarizer.main:main'
        ]
    }
)