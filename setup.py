from setuptools import setup

setup(
    name='ssher',
    version='0.1',
    author='Maxim Kirilov',
    author_email='kir.maxim@gmail.com',
    py_modules=['ssher'],
    install_requires=[
        'Click==7.1.2',
        'dependency-injector[yaml]==3.44.0',
        'pexpect==4.8.0',
    ],
    entry_points='''
        [console_scripts]
        ssher=ssher.app.main:connect
    ''',
)
