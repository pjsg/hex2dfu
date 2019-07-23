from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='hex2dfu',
      version='0.1',
      packages=['hex2dfu'],
      description='hex file converter to dfu',
      url='https://github.com/pjsg/hex2dfu',
      author='Philip Gladstone',
      install_requires=[
          'intelhex>=2.2.1',
          'markdown',
          'docopt',
      ],
      long_description=readme(),
      zip_safe=False,
      entry_points={
          'console_scripts': ['hex2dfu=hex2dfu:main'],
      })

