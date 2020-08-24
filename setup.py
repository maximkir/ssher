from setuptools import setup

setup(
    name='ssher',
    version='0.1',
    py_modules=['ssher'],
    install_requires=[
        'Click==7.1.2',
    ],
    entry_points='''
        [console_scripts]
        ssher=ssher.commands:connect
    ''',
)
