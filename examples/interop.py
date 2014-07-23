from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL import platform as gl_platform
from OpenGL import GLX

from pycl import *
import numpy as np

glutInit()
gl_window = glutCreateWindow("window")
gl_ctx = gl_platform.GetCurrentContext()
glx_display = GLX.glXGetCurrentDisplay()

cl_ctx_props = {
    CL_GL_CONTEXT_KHR:  gl_ctx,
    CL_GLX_DISPLAY_KHR: glx_display,
}
cl_ctx = clCreateContext(other_props=cl_ctx_props)
cl_queue = clCreateCommandQueue(cl_ctx)

def idle():
    input_data = np.arange(20, dtype=np.float32)

    gl_buf = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, gl_buf)
    glBufferData(GL_ARRAY_BUFFER, input_data, GL_STATIC_DRAW)
    glFinish()

    cl_buf = clCreateFromGLBuffer(cl_ctx, gl_buf)
    clEnqueueAcquireGLObjects(cl_queue, [cl_buf])

    # ... kernel, or copy back
    output_data, event = buffer_to_ndarray(cl_queue, cl_buf, like=input_data)

    clEnqueueReleaseGLObjects(cl_queue, [cl_buf])
    clFinish(cl_queue)

    np.testing.assert_equal(output_data, input_data)
    print "Interop works!"

    glutLeaveMainLoop()

glutIdleFunc(idle)
glutMainLoop()
