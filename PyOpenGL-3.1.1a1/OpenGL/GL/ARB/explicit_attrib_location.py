'''OpenGL extension ARB.explicit_attrib_location

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.explicit_attrib_location to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a method to pre-assign attribute locations to
	named vertex shader inputs and color numbers to named fragment shader
	outputs.  This allows applications to globally assign a particular
	semantic meaning, such as diffuse color or vertex normal, to a particular
	attribute location without knowing how that attribute will be named in any
	particular shader.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/explicit_attrib_location.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.explicit_attrib_location import *
from OpenGL.raw.GL.ARB.explicit_attrib_location import _EXTENSION_NAME

def glInitExplicitAttribLocationARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION