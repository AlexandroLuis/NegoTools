from setuptools import setup

setup(
    name='NegoTools', 
    version='0.5', 
    description='nego tools',
    author='Alexandro Rocha', 
    url='https://github.com/AlexandroLuis/NegoTools',
    packages=['hyperheuristic','isItWorking'], 
    install_requires=[
        'thompson-sampling'
    ],
    zip_safe=False
)