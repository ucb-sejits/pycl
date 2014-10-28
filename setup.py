from setuptools import setup

from setuptools.command.sdist import sdist
from subprocess import Popen, PIPE

from pycl import __version__

class sdist_hg(sdist):
    user_options = sdist.user_options + [
            ('dev', None, "Add a dev marker")
            ]

    def initialize_options(self):
        sdist.initialize_options(self)
        self.dev = 0

    def run(self):
        if self.dev:
            suffix = '.dev%s' % self.get_revision()
            self.distribution.metadata.version += suffix
        sdist.run(self)

    def get_revision(self):
        try:
            p = Popen(['hg', 'id', '-i'], stdout=PIPE)
            rev = p.stdout.read().strip()
        except:
            print("Could not determine hg revision.")
            rev = "deadbeef"
        return rev

setup(
    name='pycl',
    version=__version__,
    author="Ken Watford",
    author_email="kwatford@gmail.com",
    url="https://bitbucket.org/kw/pycl",
    download_url="https://bitbucket.org/kw/pycl/downloads",
    py_modules=['pycl'],
    license='MIT',
    description="OpenCL wrapper using ctypes",
    long_description=open('README.md').read(),
    tests_require=['nose'],
    cmdclass={'sdist': sdist_hg},
    classifiers = [
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
