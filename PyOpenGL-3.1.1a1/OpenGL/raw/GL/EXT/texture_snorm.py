'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_texture_snorm'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_texture_snorm',error_checker=_errors._error_checker)
GL_ALPHA16_SNORM=_C('GL_ALPHA16_SNORM',0x9018)
GL_ALPHA8_SNORM=_C('GL_ALPHA8_SNORM',0x9014)
GL_ALPHA_SNORM=_C('GL_ALPHA_SNORM',0x9010)
GL_INTENSITY16_SNORM=_C('GL_INTENSITY16_SNORM',0x901B)
GL_INTENSITY8_SNORM=_C('GL_INTENSITY8_SNORM',0x9017)
GL_INTENSITY_SNORM=_C('GL_INTENSITY_SNORM',0x9013)
GL_LUMINANCE16_ALPHA16_SNORM=_C('GL_LUMINANCE16_ALPHA16_SNORM',0x901A)
GL_LUMINANCE16_SNORM=_C('GL_LUMINANCE16_SNORM',0x9019)
GL_LUMINANCE8_ALPHA8_SNORM=_C('GL_LUMINANCE8_ALPHA8_SNORM',0x9016)
GL_LUMINANCE8_SNORM=_C('GL_LUMINANCE8_SNORM',0x9015)
GL_LUMINANCE_ALPHA_SNORM=_C('GL_LUMINANCE_ALPHA_SNORM',0x9012)
GL_LUMINANCE_SNORM=_C('GL_LUMINANCE_SNORM',0x9011)
GL_R16_SNORM=_C('GL_R16_SNORM',0x8F98)
GL_R8_SNORM=_C('GL_R8_SNORM',0x8F94)
GL_RED_SNORM=_C('GL_RED_SNORM',0x8F90)
GL_RG16_SNORM=_C('GL_RG16_SNORM',0x8F99)
GL_RG8_SNORM=_C('GL_RG8_SNORM',0x8F95)
GL_RGB16_SNORM=_C('GL_RGB16_SNORM',0x8F9A)
GL_RGB8_SNORM=_C('GL_RGB8_SNORM',0x8F96)
GL_RGBA16_SNORM=_C('GL_RGBA16_SNORM',0x8F9B)
GL_RGBA8_SNORM=_C('GL_RGBA8_SNORM',0x8F97)
GL_RGBA_SNORM=_C('GL_RGBA_SNORM',0x8F93)
GL_RGB_SNORM=_C('GL_RGB_SNORM',0x8F92)
GL_RG_SNORM=_C('GL_RG_SNORM',0x8F91)
GL_SIGNED_NORMALIZED=_C('GL_SIGNED_NORMALIZED',0x8F9C)

