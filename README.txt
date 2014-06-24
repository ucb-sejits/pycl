What is PyCL?
=============

PyCL is yet another OpenCL wrapper for Python. Its primary goal is
simple: wrap OpenCL in such a way that as many Python 
implementations can use it as feasible. It is currently tested on 
CPython 2.{5,6,7}, 3.2, and PyPy 1.5. It is known to largely not work on
Jython, whose ctypes library is still immature.

To achieve this, we eschew extension modules and dependencies
outside of the standard library. Ideally things like NumPy arrays 
and PIL images should Just Work, but they shouldn't be required. 

If you're looking to get actual work done in OpenCL, this probably 
isn't the distribution for you... yet. Before considering using PyCL for
anything, give PyOpenCL_ a look. Its API is stable, its wrapper layer
is fast C++, and it has fairly reasonable dependencies. 

If you're looking to contribute, or just get the latest development
release, take a look at our repository_.

Installation
============

It's on PyPI, so installation should be as easy as::

    pip install pycl
          -or-
    easy_install pycl

But it's a single module and there's nothing to compile,
so downloading it from PyPI_ or the repository and using 
it directly works too.

To actually use it, though, you'll need an OpenCL platform installed.
If you're on Mac OS X 10.6 or later, you're already done. Otherwise,
download and install an appropriate platform from AMD_, Intel_, or
NVIDIA_.

.. _PyOpenCL: http://mathema.tician.de/software/pyopencl
.. _repository: https://bitbucket.org/kw/pycl
.. _PyPI: http://pypi.python.org/pypi/pycl/
.. _AMD: http://developer.amd.com/zones/OpenCLZone/pages/toolsandlibraries.aspx
.. _Intel: http://software.intel.com/en-us/articles/download-intel-opencl-sdk/
.. _NVIDIA: http://developer.nvidia.com/opencl
