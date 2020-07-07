'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_transform_feedback_instanced'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_transform_feedback_instanced',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLsizei)
def glDrawTransformFeedbackInstanced(mode,id,instancecount):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei)
def glDrawTransformFeedbackStreamInstanced(mode,id,stream,instancecount):pass
