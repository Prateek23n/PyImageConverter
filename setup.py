from setuptools import setup, find_packages 
from os import path

with open('requirements.txt') as f: 
    requirements = f.readlines() 

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()  
  
setup( 
        name ='PyImageConverter', 
        version ='1.0.0', 
        author ='Prateek C. Tripathi', 
        author_email ='prateektripathi85@gmail.com', 
        url ='https://github.com/Prateek23n/PyImageConverter', 
        description ='Sample Package',
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
            ] 
        }, 
        classifiers =( 
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ), 
        keywords ='python image converter', 
        install_requires = requirements, 
        zip_safe = True
) 
