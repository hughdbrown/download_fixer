#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


def requirements():
    with open("requirements.txt") as handle:
        return [line.strip() for line in handle if not line.startswith("#")]


setup(
    name='download-fixer',
    version='0.0.1',
    description='Remove repeated files using unix softlinks',
    long_description=open("README.md").read(),
    author='Hugh Brown',
    author_email='hughdbrown@yahoo.com',
    url='http://iwebthereforeiam.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=requirements(),
    #tests_require=[
    #    'nose',
    #],
    setup_requires=[],
    packages=[
        'src',
    ],
    test_suite='nose.collector',
    zip_safe=False,
    scripts=[
        'bin/download-fixer',
    ],
    entry_points={
        'console_scripts': [
            'download-fixer = src.download_fixer:main',
        ],
    },
)
