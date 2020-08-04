from setuptools import setup, find_packages


with open('README.md') as f:
    readme_text = f.read()

with open('LICENSE') as f:
    license_text = f.read()

setup(
    name='example',
    version='0.0.1',
    description='Example OpenCV Python Exercise ',
    long_description=readme_text,
    author='AVAIRDS',
    url='https://github.com/alexsnowschool/OpenCV-with-Python',
    license=license_text)
)
