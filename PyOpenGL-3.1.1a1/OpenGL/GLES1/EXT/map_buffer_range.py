'''OpenGL extension EXT.map_buffer_range

This module customises the behaviour of the 
OpenGL.raw.GLES1.EXT.map_buffer_range to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/map_buffer_range.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.EXT.map_buffer_range import *
from OpenGL.raw.GLES1.EXT.map_buffer_range import _EXTENSION_NAME

def glInitMapBufferRangeEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION