from setuptools import setup

setup(
    name='NegoTools', 
    version='0.7', 
    description='nego tools',
    author='Alexandro Rocha', 
    url='https://github.com/AlexandroLuis/NegoTools',
    package_dir = {
    	"hyperheuristic": "hyperheuristic",
    	"Scientific": "Scientific",
    },
    packages=[
    	'hyperheuristic',
    	'Scientific',
    	'Scientific.Regression',
    	'Scientific.Clustering',
    	'Scientific.Classification',
    ],
    install_requires=[
        'thompson-sampling',
        'pandas',
        'random2',
        'numpy',
        'matplotlib',
    ],
    zip_safe=False
)
