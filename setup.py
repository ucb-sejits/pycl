from setuptools import setup

from pycl import __version__

setup(
    name='pycl',
    version=__version__,
    author="Ken Watford",
    author_email="kwatford@gmail.com",
    url="https://github.com/ucb-sejits/pycl",
    download_url="https://github.com/ucb-sejits/pycl",
    py_modules=['pycl'],
    license='MIT',
    description="OpenCL wrapper using ctypes",
    # long_description=open('README.md').read(),
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        ],
    entry_points={
        'console_scripts': ['pycl = pycl:main'],
    }

)
