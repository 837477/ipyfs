"""
IPyFS (Python IPFS Client)
"""
import setuptools
from setuptools import setup
from ipyfs import __AUTHOR__, __VERSION__

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ipyfs',
    version=__VERSION__,
    description='IPyFS, Python-based IPFS CLI.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/837477/IPyFS',
    author=__AUTHOR__,
    author_email='8374770@gmail.com',
    license='MIT',
    packages=['ipyfs', 'ipyfs.RPCs'],
    keywords=['ipyfs', 'ipfs', 'ipfs python', 'ipfs-python', 'iptf_python', 'python-ipfs', 'python_ipfs'],
    python_requires = '>=3.7',
    install_requires=['requests'],
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
