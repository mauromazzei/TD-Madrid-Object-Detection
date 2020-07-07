'''OpenGL extension ARB.shadow

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shadow to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension clarifies the GL_SGIX_shadow extension.
	
	This extension supports comparing the texture R coordinate to a depth
	texture value in order to produce a boolean texture value.  This can
	be used to implement shadow maps.
	
	The extension is written in generic terms such that other texture
	comparison modes can be accommodated in the future.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/shadow.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.shadow import *
from OpenGL.raw.GL.ARB.shadow import _EXTENSION_NAME

def glInitShadowARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION
