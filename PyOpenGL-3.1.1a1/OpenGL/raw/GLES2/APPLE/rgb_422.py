'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_APPLE_rgb_422'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_APPLE_rgb_422',error_checker=_errors._error_checker)
GL_RGB_422_APPLE=_C('GL_RGB_422_APPLE',0x8A1F)
GL_RGB_RAW_422_APPLE=_C('GL_RGB_RAW_422_APPLE',0x8A51)
GL_UNSIGNED_SHORT_8_8_APPLE=_C('GL_UNSIGNED_SHORT_8_8_APPLE',0x85BA)
GL_UNSIGNED_SHORT_8_8_REV_APPLE=_C('GL_UNSIGNED_SHORT_8_8_REV_APPLE',0x85BB)

