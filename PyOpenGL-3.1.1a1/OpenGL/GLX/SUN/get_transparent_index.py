'''OpenGL extension SUN.get_transparent_index

This module customises the behaviour of the 
OpenGL.raw.GLX.SUN.get_transparent_index to provide a more 
Python-friendly API

Overview (from the spec)
	
	Gets the transparent pixel index for an overlay/underlay window pair.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SUN/get_transparent_index.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLX import _types, _glgets
from OpenGL.raw.GLX.SUN.get_transparent_index import *
from OpenGL.raw.GLX.SUN.get_transparent_index import _EXTENSION_NAME

def glInitGetTransparentIndexSUN():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION