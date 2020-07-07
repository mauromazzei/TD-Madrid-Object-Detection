'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIS_multisample'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_SGIS_multisample',error_checker=_errors._error_checker)
GL_1PASS_SGIS=_C('GL_1PASS_SGIS',0x80A1)
GL_2PASS_0_SGIS=_C('GL_2PASS_0_SGIS',0x80A2)
GL_2PASS_1_SGIS=_C('GL_2PASS_1_SGIS',0x80A3)
GL_4PASS_0_SGIS=_C('GL_4PASS_0_SGIS',0x80A4)
GL_4PASS_1_SGIS=_C('GL_4PASS_1_SGIS',0x80A5)
GL_4PASS_2_SGIS=_C('GL_4PASS_2_SGIS',0x80A6)
GL_4PASS_3_SGIS=_C('GL_4PASS_3_SGIS',0x80A7)
GL_MULTISAMPLE_SGIS=_C('GL_MULTISAMPLE_SGIS',0x809D)
GL_SAMPLES_SGIS=_C('GL_SAMPLES_SGIS',0x80A9)
GL_SAMPLE_ALPHA_TO_MASK_SGIS=_C('GL_SAMPLE_ALPHA_TO_MASK_SGIS',0x809E)
GL_SAMPLE_ALPHA_TO_ONE_SGIS=_C('GL_SAMPLE_ALPHA_TO_ONE_SGIS',0x809F)
GL_SAMPLE_BUFFERS_SGIS=_C('GL_SAMPLE_BUFFERS_SGIS',0x80A8)
GL_SAMPLE_MASK_INVERT_SGIS=_C('GL_SAMPLE_MASK_INVERT_SGIS',0x80AB)
GL_SAMPLE_MASK_SGIS=_C('GL_SAMPLE_MASK_SGIS',0x80A0)
GL_SAMPLE_MASK_VALUE_SGIS=_C('GL_SAMPLE_MASK_VALUE_SGIS',0x80AA)
GL_SAMPLE_PATTERN_SGIS=_C('GL_SAMPLE_PATTERN_SGIS',0x80AC)
@_f
@_p.types(None,_cs.GLclampf,_cs.GLboolean)
def glSampleMaskSGIS(value,invert):pass
@_f
@_p.types(None,_cs.GLenum)
def glSamplePatternSGIS(pattern):pass
