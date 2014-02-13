from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='vs.urllib2timeout',
      version=version,
      description="Sets a default timeout on urllib2.urlopen.",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='THijs',
      author_email='thijs.jonkman@virtualsciences.nl',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['vs', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
