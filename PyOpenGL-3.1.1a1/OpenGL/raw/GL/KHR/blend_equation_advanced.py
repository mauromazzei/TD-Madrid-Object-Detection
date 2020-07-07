'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_KHR_blend_equation_advanced'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_KHR_blend_equation_advanced',error_checker=_errors._error_checker)
GL_COLORBURN_KHR=_C('GL_COLORBURN_KHR',0x929A)
GL_COLORDODGE_KHR=_C('GL_COLORDODGE_KHR',0x9299)
GL_DARKEN_KHR=_C('GL_DARKEN_KHR',0x9297)
GL_DIFFERENCE_KHR=_C('GL_DIFFERENCE_KHR',0x929E)
GL_EXCLUSION_KHR=_C('GL_EXCLUSION_KHR',0x92A0)
GL_HARDLIGHT_KHR=_C('GL_HARDLIGHT_KHR',0x929B)
GL_HSL_COLOR_KHR=_C('GL_HSL_COLOR_KHR',0x92AF)
GL_HSL_HUE_KHR=_C('GL_HSL_HUE_KHR',0x92AD)
GL_HSL_LUMINOSITY_KHR=_C('GL_HSL_LUMINOSITY_KHR',0x92B0)
GL_HSL_SATURATION_KHR=_C('GL_HSL_SATURATION_KHR',0x92AE)
GL_LIGHTEN_KHR=_C('GL_LIGHTEN_KHR',0x9298)
GL_MULTIPLY_KHR=_C('GL_MULTIPLY_KHR',0x9294)
GL_OVERLAY_KHR=_C('GL_OVERLAY_KHR',0x9296)
GL_SCREEN_KHR=_C('GL_SCREEN_KHR',0x9295)
GL_SOFTLIGHT_KHR=_C('GL_SOFTLIGHT_KHR',0x929C)
@_f
@_p.types(None,)
def glBlendBarrierKHR():pass
