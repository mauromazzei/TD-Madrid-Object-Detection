'''OpenGL extension ARB.vertex_array_object

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.vertex_array_object to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension introduces named vertex array objects which encapsulate
	vertex array state on the client side.  These objects allow applications
	to rapidly switch between large sets of array state.  In addition, layered
	libraries can return to the default array state by simply creating and
	binding a new vertex array object.
	
	This extension differs from GL_APPLE_vertex_array_object in that client
	memory cannot be accessed through a non-zero vertex array object.  It also
	differs in that vertex array objects are explicitly not sharable between
	contexts.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/vertex_array_object.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.vertex_array_object import *
from OpenGL.raw.GL.ARB.vertex_array_object import _EXTENSION_NAME

def glInitVertexArrayObjectARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glDeleteVertexArrays.arrays size not checked against n
glDeleteVertexArrays=wrapper.wrapper(glDeleteVertexArrays).setInputArraySize(
    'arrays', None
)
glGenVertexArrays=wrapper.wrapper(glGenVertexArrays).setOutput(
    'arrays',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
### END AUTOGENERATED SECTION

glGenVertexArrays = wrapper.wrapper(glGenVertexArrays).setOutput(
    'arrays', lambda n, array=None: (n,), 'n', arrayType = arrays.GLuintArray,
    orPassIn=True,
)
