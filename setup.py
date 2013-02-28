import os
from setuptools import setup, find_packages


def read_file(filename):
    basepath = os.path.dirname(os.path.dirname(__file__))
    filepath = os.path.join(basepath, filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''


setup (
    name='mahokanta',
    version='0.0.1',
    description='A Web-Server to view HTTP-Request as raw text',
    long_description=read_file('README.rst'),
    author='kjirou',
    author_email='sorenariblog@gmail.com',
    url='https://github.com/kjirou/python-mahokanta',
    packages=find_packages(),
    install_requires=['webob'],
    entry_points={
        'console_scripts': [
            'mahokanta=mahokanta.server:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords=['http', 'tool', 'command'],
    license='MIT License',
)
