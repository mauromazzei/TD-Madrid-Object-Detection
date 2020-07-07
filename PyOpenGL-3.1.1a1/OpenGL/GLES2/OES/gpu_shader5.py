'''OpenGL extension OES.gpu_shader5

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.gpu_shader5 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/gpu_shader5.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.gpu_shader5 import *
from OpenGL.raw.GLES2.OES.gpu_shader5 import _EXTENSION_NAME

def glInitGpuShader5OES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION