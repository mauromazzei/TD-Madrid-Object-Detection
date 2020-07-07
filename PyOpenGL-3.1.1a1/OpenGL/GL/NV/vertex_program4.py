'''OpenGL extension NV.vertex_program4

This module customises the behaviour of the 
OpenGL.raw.GL.NV.vertex_program4 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension builds on the common assembly instruction set
	infrastructure provided by NV_gpu_program4, adding vertex program-specific
	features.
	
	This extension provides the ability to specify integer vertex attributes
	that are passed to vertex programs using integer data types, rather than
	being converted to floating-point values as in existing vertex attribute
	functions.  The set of input and output bindings provided includes all
	bindings supported by ARB_vertex_program.  This extension provides
	additional input bindings identifying the index of the vertex when vertex
	arrays are used ("vertex.id") and the instance number when instanced
	arrays are used ("vertex.instance", requires EXT_draw_instanced).  It
	also provides output bindings allowing vertex programs to directly specify
	clip distances (for user clipping) plus a set of generic attributes that
	allow programs to pass a greater number of attributes to subsequent
	pipeline stages than is possible using only the pre-defined fixed-function
	vertex outputs.
	
	By and large, programs written to ARB_vertex_program can be ported
	directly by simply changing the program header from "!!ARBvp1.0" to
	"!!NVvp4.0", and then modifying instructions to take advantage of the
	expanded feature set.  There are a small number of areas where this
	extension is not a functional superset of previous vertex program
	extensions, which are documented in the NV_gpu_program4 specification.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/vertex_program4.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.vertex_program4 import *
from OpenGL.raw.GL.NV.vertex_program4 import _EXTENSION_NAME

def glInitVertexProgram4NV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glVertexAttribI1ivEXT=wrapper.wrapper(glVertexAttribI1ivEXT).setInputArraySize(
    'v', 1
)
glVertexAttribI2ivEXT=wrapper.wrapper(glVertexAttribI2ivEXT).setInputArraySize(
    'v', 2
)
glVertexAttribI3ivEXT=wrapper.wrapper(glVertexAttribI3ivEXT).setInputArraySize(
    'v', 3
)
glVertexAttribI4ivEXT=wrapper.wrapper(glVertexAttribI4ivEXT).setInputArraySize(
    'v', 4
)
glVertexAttribI1uivEXT=wrapper.wrapper(glVertexAttribI1uivEXT).setInputArraySize(
    'v', 1
)
glVertexAttribI2uivEXT=wrapper.wrapper(glVertexAttribI2uivEXT).setInputArraySize(
    'v', 2
)
glVertexAttribI3uivEXT=wrapper.wrapper(glVertexAttribI3uivEXT).setInputArraySize(
    'v', 3
)
glVertexAttribI4uivEXT=wrapper.wrapper(glVertexAttribI4uivEXT).setInputArraySize(
    'v', 4
)
glVertexAttribI4bvEXT=wrapper.wrapper(glVertexAttribI4bvEXT).setInputArraySize(
    'v', 4
)
glVertexAttribI4svEXT=wrapper.wrapper(glVertexAttribI4svEXT).setInputArraySize(
    'v', 4
)
glVertexAttribI4ubvEXT=wrapper.wrapper(glVertexAttribI4ubvEXT).setInputArraySize(
    'v', 4
)
glVertexAttribI4usvEXT=wrapper.wrapper(glVertexAttribI4usvEXT).setInputArraySize(
    'v', 4
)
# INPUT glVertexAttribIPointerEXT.pointer size not checked against 'size,type,stride'
glVertexAttribIPointerEXT=wrapper.wrapper(glVertexAttribIPointerEXT).setInputArraySize(
    'pointer', None
)
glGetVertexAttribIivEXT=wrapper.wrapper(glGetVertexAttribIivEXT).setOutput(
    'params',size=(1,),orPassIn=True
)
glGetVertexAttribIuivEXT=wrapper.wrapper(glGetVertexAttribIuivEXT).setOutput(
    'params',size=(1,),orPassIn=True
)
### END AUTOGENERATED SECTION