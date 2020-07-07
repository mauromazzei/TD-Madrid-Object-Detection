'''OpenGL extension AMD.seamless_cubemap_per_texture

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.seamless_cubemap_per_texture to provide a more 
Python-friendly API

Overview (from the spec)
	
	In unextended OpenGL, cube maps are treated as sets of six, independent
	texture images. Once a face is selected from the set, it is treated exactly
	as any other two-dimensional texture would be. When sampling linearly from
	the texture, all of the individual texels that would be used to to create
	the final, bilinear sample values are taken from the same cube face. The
	normal, two-dimensional texture coordinate wrapping modes are honored.
	This sometimes causes seams to appear in cube maps.
	
	ARB_seamless_cube_map addresses this issue by providing a mechanism whereby
	an implementation could take each of the taps of a bilinear sample from
	a different face, spanning face boundaries and providing seamless filtering
	from cube map textures. However, in ARB_seamless_cube_map, this feature was
	exposed as a global state, affecting all bound cube map textures. It was not
	possible to mix seamless and per-face cube map sampling modes during
	multisampling. Furthermore, if an application included cube maps that were
	meant to be sampled seamlessly and non-seamlessly, it would have to track
	this state and enable or disable seamless cube map sampling as needed.
	
	This extension addresses this issue and provides an orthogonal method for
	allowing an implementation to provide a per-texture setting for enabling
	seamless sampling from cube maps.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/seamless_cubemap_per_texture.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.seamless_cubemap_per_texture import *
from OpenGL.raw.GL.AMD.seamless_cubemap_per_texture import _EXTENSION_NAME

def glInitSeamlessCubemapPerTextureAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION