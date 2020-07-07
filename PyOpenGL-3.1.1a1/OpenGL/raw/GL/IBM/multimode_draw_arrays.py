'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_IBM_multimode_draw_arrays'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_IBM_multimode_draw_arrays',error_checker=_errors._error_checker)

@_f
@_p.types(None,arrays.GLuintArray,arrays.GLintArray,arrays.GLsizeiArray,_cs.GLsizei,_cs.GLint)
def glMultiModeDrawArraysIBM(mode,first,count,primcount,modestride):pass
@_f
@_p.types(None,arrays.GLuintArray,arrays.GLsizeiArray,_cs.GLenum,arrays.GLvoidpArray,_cs.GLsizei,_cs.GLint)
def glMultiModeDrawElementsIBM(mode,count,type,indices,primcount,modestride):pass
