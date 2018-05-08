from setuptools import setup, find_packages

setup(name='perforate',
      version='0.0.1',
      description='Python connector for Perforate',
      author='Alexander Tereshkin',
      author_email='atereshkin@y-node.com',
      url='https://github.com/atereshkin/perforate-python',
      packages=['perforate'],
      install_requires=['protobuf>=3.0.0', 'pyzmq>=17.0.0']
     )
