'''OpenGL extension EXT.vertex_shader

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.vertex_shader to provide a more 
Python-friendly API

Overview (from the spec)
	
	EXT_vertex_shader adds a flexible way to change the per-vertex
	processing in the GL pipeline. It provides a method to replace
	the fixed vertex/normal transform and lighting with a user
	specified means of generating processed vertices, texture
	coordinates, color, and secondary color, along with a primitive's
	associated state.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/vertex_shader.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.vertex_shader import *
from OpenGL.raw.GL.EXT.vertex_shader import _EXTENSION_NAME

def glInitVertexShaderEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glSetInvariantEXT.addr size not checked against 'id,type'
glSetInvariantEXT=wrapper.wrapper(glSetInvariantEXT).setInputArraySize(
    'addr', None
)
# INPUT glSetLocalConstantEXT.addr size not checked against 'id,type'
glSetLocalConstantEXT=wrapper.wrapper(glSetLocalConstantEXT).setInputArraySize(
    'addr', None
)
# INPUT glVariantbvEXT.addr size not checked against 'id'
glVariantbvEXT=wrapper.wrapper(glVariantbvEXT).setInputArraySize(
    'addr', None
)
# INPUT glVariantsvEXT.addr size not checked against 'id'
glVariantsvEXT=wrapper.wrapper(glVariantsvEXT).setInputArraySize(
    'addr', None
)
# INPUT glVariantivEXT.addr size not checked against 'id'
glVariantivEXT=wrapper.wrapper(glVariantivEXT).setInputArraySize(
    'addr', None
)
# INPUT glVariantfvEXT.addr size not checked against 'id'
glVariantfvEXT=wrapper.wrapper(glVariantfvEXT).setInputArraySize(
    'addr', None
)
# INPUT glVariantdvEXT.addr size not checked against 'id'
glVariantdvEXT=wrapper.wrapper(glVariantdvEXT).setInputArraySize(
    'addr', None
)
# INPUT glVariantubvEXT.addr size not checked against 'id'
glVariantubvEXT=wrapper.wrapper(glVariantubvEXT).setInputArraySize(
    'addr', None
)
# INPUT glVariantusvEXT.addr size not checked against 'id'
glVariantusvEXT=wrapper.wrapper(glVariantusvEXT).setInputArraySize(
    'addr', None
)
# INPUT glVariantuivEXT.addr size not checked against 'id'
glVariantuivEXT=wrapper.wrapper(glVariantuivEXT).setInputArraySize(
    'addr', None
)
# INPUT glVariantPointerEXT.addr size not checked against 'id,type,stride'
glVariantPointerEXT=wrapper.wrapper(glVariantPointerEXT).setInputArraySize(
    'addr', None
)
glGetVariantBooleanvEXT=wrapper.wrapper(glGetVariantBooleanvEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='id',orPassIn=True
)
glGetVariantIntegervEXT=wrapper.wrapper(glGetVariantIntegervEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='id',orPassIn=True
)
glGetVariantFloatvEXT=wrapper.wrapper(glGetVariantFloatvEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='id',orPassIn=True
)
glGetVariantPointervEXT=wrapper.wrapper(glGetVariantPointervEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='id',orPassIn=True
)
glGetInvariantBooleanvEXT=wrapper.wrapper(glGetInvariantBooleanvEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='id',orPassIn=True
)
glGetInvariantIntegervEXT=wrapper.wrapper(glGetInvariantIntegervEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='id',orPassIn=True
)
glGetInvariantFloatvEXT=wrapper.wrapper(glGetInvariantFloatvEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='id',orPassIn=True
)
glGetLocalConstantBooleanvEXT=wrapper.wrapper(glGetLocalConstantBooleanvEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='id',orPassIn=True
)
glGetLocalConstantIntegervEXT=wrapper.wrapper(glGetLocalConstantIntegervEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='id',orPassIn=True
)
glGetLocalConstantFloatvEXT=wrapper.wrapper(glGetLocalConstantFloatvEXT).setOutput(
    'data',size=_glgets._glget_size_mapping,pnameArg='id',orPassIn=True
)
### END AUTOGENERATED SECTION