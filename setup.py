from setuptools import setup

setup(name='consul-py',
      version='0.1',
      description='Consul client for python',
      url='https://github.com/tbt-post/consul-py',
      author='Oleg Noga',
      author_email='oleg.noga@gmail.com',
      license='MIT',
      packages=['consul'],
      install_requires=['requests'])
