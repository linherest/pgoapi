#!/usr/bin/env python

import os
from setuptools import setup, find_packages

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

setup_dir = os.path.dirname(os.path.realpath(__file__))
path_req = os.path.join(setup_dir, 'requirements.txt')
install_reqs = parse_requirements(path_req)

reqs = [str(ir.req) for ir in install_reqs]

setup(name='pgoapi',
      author = 'tjado',
      description = 'Pokemon Go API lib',
      version = '2.14.0',
      url = 'https://github.com/goedzo/pgoapi',
      download_url = "https://github.com/pogodevorg/pgoapi/releases",
      packages = find_packages(),
      install_requires = reqs
      )
