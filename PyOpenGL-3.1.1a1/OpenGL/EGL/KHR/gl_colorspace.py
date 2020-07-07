'''OpenGL extension KHR.gl_colorspace

This module customises the behaviour of the 
OpenGL.raw.EGL.KHR.gl_colorspace to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/KHR/gl_colorspace.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.KHR.gl_colorspace import *
from OpenGL.raw.EGL.KHR.gl_colorspace import _EXTENSION_NAME

def glInitGlColorspaceKHR():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION