from setuptools import find_packages,setup
from typing import List

e_dot='-e .'

def get_requirements(file_path : str)->List[str]:
    '''
    This function will return list of requirements(packeges).
    '''
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if e_dot in requirements:
            requirements.remove(e_dot)
    return requirements
setup(
    name='FirstMLProject',
    version='0.0.1',
    author='nalden141',
    author_email='noor15511551@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),




)