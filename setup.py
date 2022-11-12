from setuptools import find_packages,setup
from typing import List
import os

def get_requirements() ->List[str]:
      """
      This function return the list of required library which specified in the requirements file
      
      """
      requirement_list:list[str] = []
      # for i in os.listdir(path of requirements.txt file):
      #       requirement_list.append(i)
      return requirement_list
            
      

setup(name='sensor',
      version="0.0.1",
      author="irshad",
      author_email="m3irshad3@gmail.com",
      packages=find_packages(),
      install_requires=  get_requirements() #[],
      )