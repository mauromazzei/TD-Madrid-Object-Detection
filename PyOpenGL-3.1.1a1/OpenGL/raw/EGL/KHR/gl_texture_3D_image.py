'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_KHR_gl_texture_3D_image'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.EGL,'EGL_KHR_gl_texture_3D_image',error_checker=_errors._error_checker)
EGL_GL_TEXTURE_3D_KHR=_C('EGL_GL_TEXTURE_3D_KHR',0x30B2)
EGL_GL_TEXTURE_ZOFFSET_KHR=_C('EGL_GL_TEXTURE_ZOFFSET_KHR',0x30BD)

