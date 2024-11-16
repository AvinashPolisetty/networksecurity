from setuptools import find_packages,setup
from typing import List

Hypen_e_dot="-e ."

def get_requirements(file_path:str)->List:
    requirements=[]

    try:
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n","") for req in requirements]
            
            if Hypen_e_dot in requirements:
                requirements.remove(Hypen_e_dot)

    except FileNotFoundError:
        print('requirements.txt is not found')

    return requirements

setup(
    name="Network Security",
    version="0.0.1",
    description="An end to end AI project",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)