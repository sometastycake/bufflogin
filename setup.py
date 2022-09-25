import setuptools
from setuptools import setup


requirements = [
    'lxml>=4.9.1',
    'pysteamauth>=0.0.5',
    'cssselect>=1.1.0',
]


setup(
    name='bufflogin',
    version='0.0.2',
    url='https://github.com/sometastycake/bufflogin',
    license='MIT',
    author='Mike M',
    author_email='stopthisworldplease@outlook.com',
    description='Authorization to buff.163.com through Steam',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=requirements,
    include_package_data=True,
)
