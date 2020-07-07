'''OpenGL extension NV.draw_buffers

This module customises the behaviour of the 
OpenGL.raw.GLES2.NV.draw_buffers to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/draw_buffers.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.NV.draw_buffers import *
from OpenGL.raw.GLES2.NV.draw_buffers import _EXTENSION_NAME

def glInitDrawBuffersNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glDrawBuffersNV.bufs size not checked against n
glDrawBuffersNV=wrapper.wrapper(glDrawBuffersNV).setInputArraySize(
    'bufs', None
)
### END AUTOGENERATED SECTION