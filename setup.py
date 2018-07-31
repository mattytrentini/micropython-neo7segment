import io
import os
from setuptools import setup

DESCRIPTION = 'Driver for the Neo7Segment display device'

here = os.path.abspath(os.path.dirname(__file__))
# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(name='micropython-neo7segment',
      version='0.1',
      description=DESCRIPTION,
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Matt Trentini',
      author_email='matt.trentini@gmail.com',
      license='MIT',
      url='https://github.com/mattytrentini/micropython-neo7segment',
      packages=['neo7segment']
     )