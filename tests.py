from nose import SkipTest
from pycl import *
from array import array
import abc

try:
    import numpy
except ImportError:
    numpy = None


class BaseTest(object):
    source = """
    kernel void mxplusb(float m, global float *x, float b, global float *out) {
        int i = get_global_id(0);
        out[i] = m*x[i]+b;
    }
    """

    @abc.abstractmethod
    def check(self, queue, kernel):
        """Function that tests data references"""
        return

    def test(self):
        for platform in clGetPlatformIDs():
            context = clCreateContext(platform=platform)
            queue = clCreateCommandQueue(context)
            program = clCreateProgramWithSource(context, self.source).build()
            kernel = program['mxplusb']
            kernel.argtypes = (cl_float, cl_mem, cl_float, cl_mem)            
            yield self.check, queue, kernel        


class TestNumpy(BaseTest):
    def check(self, queue, kernel):
        if not numpy:
            raise SkipTest

        m = 2
        b = 5
        x = numpy.arange(100, dtype='float32')
        x_buf, in_evt = buffer_from_ndarray(queue, x, blocking=False)
        y_buf = x_buf.empty_like_this()
        run_evt = kernel(m, x_buf, b, y_buf).on(queue, x.size, wait_for=in_evt)
        y, evt = buffer_to_ndarray(queue, y_buf, wait_for=run_evt, like=x)
        evt.wait()
        assert(numpy.allclose(y, m*x+b))


def assert_sequence_almost_equal(x, y, tol=1e-7):
    assert len(x) == len(y), "Lengths not equal"
    for (i, (xi, yi)) in enumerate(zip(x, y)):
        assert abs(xi - yi) < tol, "Sequences differ starting at element %d" % i


class TestPyArray(BaseTest):
    def check(self, queue, kernel):
        m = 2
        b = 5
        x = array('f', range(100))
        x_buf, in_evt = buffer_from_pyarray(queue, x, blocking=False)
        y_buf = x_buf.empty_like_this()
        run_evt = kernel(m, x_buf, b, y_buf).on(queue, len(x), wait_for=in_evt)
        y, evt = buffer_to_pyarray(queue, y_buf, wait_for=run_evt, like=x)
        evt.wait()
        y2 = array('f', (m*xi+b for xi in x))
        assert_sequence_almost_equal(y, y2)


class TestCopyBuffer(BaseTest):
    def check(self, queue, kernel):
        if not numpy:
            raise SkipTest

        expected = numpy.arange(10)
        src_buf, evt = buffer_from_ndarray(queue, expected)
        dst_buf, evt = buffer_from_ndarray(queue, numpy.ones_like(expected))
        clEnqueueCopyBuffer(queue, src_buf, dst_buf)
        answer, evt = buffer_to_ndarray(queue, dst_buf, shape=expected.shape, dtype=expected.dtype)
        numpy.testing.assert_equal(answer, expected)
