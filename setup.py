from setuptools import setup

setup(
    name='NegoTools', 
    version='0.3', 
    description='nego tools',
    author='Alexandro Rocha', 
    package=['hyperheuristic'], 
    install_requires=[
        'thompson-sampling'
    ],
    zip_safe=False
)