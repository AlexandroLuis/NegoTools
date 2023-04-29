from setuptools import setup

setup(
    name='NegoTools', 
    version='0.8', 
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
    	'Scientific.Clustering',
    ],
    install_requires=[
        'thompson-sampling',
        'pandas',
        'random2',
        'numpy',
        'matplotlib',
        'scikit-learn'
    ],
    zip_safe=False
)
