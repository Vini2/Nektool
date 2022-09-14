from setuptools import setup

CLASSIFIERS = [
    "Environment :: Console",
    "Environment :: MacOS X",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: {{cookiecutter.license}}",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]

setup(
 name='{{cookiecutter.project_name}}',
 description="{{cookiecutter.project_description}}",
 version='{{cookiecutter.project_slug}}',
 author="{{cookiecutter.full_name}}",
 author_email="{{cookiecutter.email}}",
 py_modules=['{{cookiecutter.project_slug}}'],
 install_requires=['Click>=7', 'nextflow>=0.4.0', 'pyyaml>=6'],
 entry_points={
  'console_scripts': [
    '{{cookiecutter.project_slug}}={{cookiecutter.project_slug}}.__main__:main'
  ]},
 include_package_data=True,
)