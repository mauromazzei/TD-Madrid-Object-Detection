'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES1 import _types as _cs
# End users want this...
from OpenGL.raw.GLES1._types import *
from OpenGL.raw.GLES1 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES1_EXT_discard_framebuffer'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES1,'GLES1_EXT_discard_framebuffer',error_checker=_errors._error_checker)
GL_COLOR_EXT=_C('GL_COLOR_EXT',0x1800)
GL_DEPTH_EXT=_C('GL_DEPTH_EXT',0x1801)
GL_STENCIL_EXT=_C('GL_STENCIL_EXT',0x1802)
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,arrays.GLuintArray)
def glDiscardFramebufferEXT(target,numAttachments,attachments):pass
