'''OpenGL extension SGIS.texture_color_mask

This module customises the behaviour of the 
OpenGL.raw.GL.SGIS.texture_color_mask to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension implements the same functionality for texture
	updates that glColorMask implements for color buffer updates.
	Masks for updating textures with indexed internal formats
	(the analog for glIndexMask) should be supported by a separate extension.
	
	The extension allows an application to update a subset of
	components in an existing texture.	The masks are applied after
	all pixel transfer operations have been performed, immediately
	prior to writing the texel value into texture memory.  They
	apply to all texture updates.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIS/texture_color_mask.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIS.texture_color_mask import *
from OpenGL.raw.GL.SGIS.texture_color_mask import _EXTENSION_NAME

def glInitTextureColorMaskSGIS():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION