'''OpenGL extension EXT.texture_sRGB_decode

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.texture_sRGB_decode to provide a more 
Python-friendly API

Overview (from the spec)
	
	The EXT_texture_sRGB extension (promoted to core in OpenGL 2.1)
	provides a texture format stored in the sRGB color space. Sampling one
	of these textures will always return the color value decoded into a
	linear color space. However, an application may wish to sample and
	retrieve the undecoded sRGB data from the texture and manipulate
	that directly.
	
	This extension adds a Texture Parameter and Sampler Object parameter to
	allow sRGB textures to be read directly, without decoding.
	
	The new parameter, TEXTURE_SRGB_DECODE_EXT controls whether the 
	decoding happens at sample time. It only applies to textures with an 
	internal format that is sRGB and is ignored for all other textures. 
	This value defaults to DECODE_EXT, which indicates the texture 
	should be decoded to linear color space.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/texture_sRGB_decode.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.texture_sRGB_decode import *
from OpenGL.raw.GLES2.EXT.texture_sRGB_decode import _EXTENSION_NAME

def glInitTextureSrgbDecodeEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION