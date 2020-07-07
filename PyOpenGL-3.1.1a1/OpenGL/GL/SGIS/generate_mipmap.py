'''OpenGL extension SGIS.generate_mipmap

This module customises the behaviour of the 
OpenGL.raw.GL.SGIS.generate_mipmap to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension defines a mechanism by which OpenGL can derive the
	entire set of mipmap arrays when provided with only the base level
	array.  Automatic mipmap generation is particularly useful when
	texture images are being provided as a video stream.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIS/generate_mipmap.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIS.generate_mipmap import *
from OpenGL.raw.GL.SGIS.generate_mipmap import _EXTENSION_NAME

def glInitGenerateMipmapSGIS():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION