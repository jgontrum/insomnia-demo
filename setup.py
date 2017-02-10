from setuptools import setup

setup(
    name='insomnia_demo_api',
    version='0.1',
    description='Demo API to reproduce a unicode error in the latest version.',
    author='Johannes Gontrum',
    author_email='gontrum@me.com',
    include_package_data=True,
    license='MIT license',
    entry_points={
          'console_scripts': [
              'start = insomnia_demo_api.scripts.start:run',
              'start_debug = insomnia_demo_api.scripts.start:run_debug'
          ]
      }
)
