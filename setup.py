from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='competitivepython',
    version='0.0.1',
    description='A collection of algorithms for competitive programming',
    author='Shikha Pandey',
    author_email='shikha.py36@gmail.com',
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/Shikha-code36/competitivepython',
    packages=find_packages(),
    install_requires=[],
    keywords=['competitive programming algorithm', 'python', 'data-structures', 'algorithms',
              'searching-algorithm', 'sorting-algorithm', 'graphs', 'binary-search tree'],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
