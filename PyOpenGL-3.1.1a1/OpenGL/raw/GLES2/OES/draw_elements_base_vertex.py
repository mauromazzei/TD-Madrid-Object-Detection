'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_OES_draw_elements_base_vertex'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_OES_draw_elements_base_vertex',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLint)
def glDrawElementsBaseVertexOES(mode,count,type,indices,basevertex):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLsizei,_cs.GLint)
def glDrawElementsInstancedBaseVertexOES(mode,count,type,indices,instancecount,basevertex):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p,_cs.GLint)
def glDrawRangeElementsBaseVertexOES(mode,start,end,count,type,indices,basevertex):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLsizeiArray,_cs.GLenum,arrays.GLvoidpArray,_cs.GLsizei,arrays.GLintArray)
def glMultiDrawElementsBaseVertexOES(mode,count,type,indices,primcount,basevertex):pass
