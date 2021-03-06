'''OpenGL extension NV.framebuffer_mixed_samples

This module customises the behaviour of the 
OpenGL.raw.GL.NV.framebuffer_mixed_samples to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/framebuffer_mixed_samples.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.framebuffer_mixed_samples import *
from OpenGL.raw.GL.NV.framebuffer_mixed_samples import _EXTENSION_NAME

def glInitFramebufferMixedSamplesNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION