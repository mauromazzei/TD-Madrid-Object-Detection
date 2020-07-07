'''OpenGL extension OES.primitive_bounding_box

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.primitive_bounding_box to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/primitive_bounding_box.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.primitive_bounding_box import *
from OpenGL.raw.GLES2.OES.primitive_bounding_box import _EXTENSION_NAME

def glInitPrimitiveBoundingBoxOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION