#!/usr/bin/env python


from setuptools import setup

meta = {}
exec(open('./streak/version.py').read(), meta)
meta['long_description'] = open('./README.md').read()

setup(
    name='python-streak',
    version=meta['__version__'],
    description='CLI to create github streaks.',
    long_description=meta['long_description'],
    long_description_content_type='text/markdown',
    keywords='streak cli git',
    author='Bastian Venthur',
    author_email='mail@venthur.de',
    url='https://github.com/venthur/streak',
    python_requires='>=3.6',
    packages=['streak'],
    entry_points={
        'console_scripts': [
            'streak = streak.streak:main'
        ]
    },
    license='MIT',
)
