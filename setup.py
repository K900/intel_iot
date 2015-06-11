from setuptools import setup, find_packages

setup(
    name='intel_iot',
    description = ('A library for interfacing with Intel IoT hardware based on the Quark SoC from Python 3.'),
    long_description = open('README.md').read(),
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['iot-shell=intel_iot.shell:main'],
    },
    extras_require={
        'shell': ["IPython"]
    },
    license='MIT', 
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License"
    ],
    keywords = ['intel', 'edison', 'mraa', 'gpio']
 )
