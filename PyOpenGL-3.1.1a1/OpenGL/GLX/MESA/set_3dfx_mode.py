'''OpenGL extension MESA.set_3dfx_mode

This module customises the behaviour of the 
OpenGL.raw.GLX.MESA.set_3dfx_mode to provide a more 
Python-friendly API

Overview (from the spec)
	
	The Mesa Glide driver allows full-screen rendering or rendering into
	an X window.  The glXSet3DfxModeMESA() function allows an application
	to switch between full-screen and windowed rendering.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/MESA/set_3dfx_mode.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLX import _types, _glgets
from OpenGL.raw.GLX.MESA.set_3dfx_mode import *
from OpenGL.raw.GLX.MESA.set_3dfx_mode import _EXTENSION_NAME

def glInitSet3DfxModeMESA():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION