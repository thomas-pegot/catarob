#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(name='catarob',
      version='1.0',
      author='Thomas Pegot',
      author_email='thomas.pegot@gmail.com',
      url='http://thomas-pegot.github.io/catarob/',
      description='Catarob GUI software',
      platforms=['Linux'],
      license='GPL v3',
      packages=['catarob', 'catarob.core', 'catarob.gui', 'catarob.lib',
                'test'],
      package_data={'test': ['data/*'], 'catarob.core': ['*.so']},
      data_files=[('docs', ['manual.pdf'])])
