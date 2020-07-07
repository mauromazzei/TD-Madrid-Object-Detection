'''OpenGL extension OES.draw_texture

This module customises the behaviour of the 
OpenGL.raw.GLES1.OES.draw_texture to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/draw_texture.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.OES.draw_texture import *
from OpenGL.raw.GLES1.OES.draw_texture import _EXTENSION_NAME

def glInitDrawTextureOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION