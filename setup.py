from setuptools import setup

README = open('README.md').read()
REQUIREMENTS = open('requirements.txt').read().splitlines()

setup(name='pypentago',
      classifiers=['Programming Language :: Python :: 3 :: Only',
                   'Topic :: Games/Entertainment'],
      version='0.1',
      description='A Pentago implementation in Python3.',
      long_description=README,
      url='http://github.com/Ball-Man/PyPentago',
      author='Francesco Mistri, Eugenio Amato Nadaia',
      author_email='franc.mistri@gmail.com',
      license='MIT',
      packages=['pypentago'],
      package_data={'pypentago': ['data/title.txt']},
      entry_points={
        'console_scripts': [
          'pypentago = pypentago.__main__:main'
        ]
      },
      install_requires=REQUIREMENTS
      )
