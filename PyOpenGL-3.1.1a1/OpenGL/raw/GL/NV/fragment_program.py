'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_fragment_program'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_fragment_program',error_checker=_errors._error_checker)
GL_FRAGMENT_PROGRAM_BINDING_NV=_C('GL_FRAGMENT_PROGRAM_BINDING_NV',0x8873)
GL_FRAGMENT_PROGRAM_NV=_C('GL_FRAGMENT_PROGRAM_NV',0x8870)
GL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV=_C('GL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV',0x8868)
GL_MAX_TEXTURE_COORDS_NV=_C('GL_MAX_TEXTURE_COORDS_NV',0x8871)
GL_MAX_TEXTURE_IMAGE_UNITS_NV=_C('GL_MAX_TEXTURE_IMAGE_UNITS_NV',0x8872)
GL_PROGRAM_ERROR_STRING_NV=_C('GL_PROGRAM_ERROR_STRING_NV',0x8874)
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLubyteArray,arrays.GLdoubleArray)
def glGetProgramNamedParameterdvNV(id,len,name,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLubyteArray,arrays.GLfloatArray)
def glGetProgramNamedParameterfvNV(id,len,name,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLubyteArray,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glProgramNamedParameter4dNV(id,len,name,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLubyteArray,arrays.GLdoubleArray)
def glProgramNamedParameter4dvNV(id,len,name,v):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLubyteArray,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glProgramNamedParameter4fNV(id,len,name,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei,arrays.GLubyteArray,arrays.GLfloatArray)
def glProgramNamedParameter4fvNV(id,len,name,v):pass
