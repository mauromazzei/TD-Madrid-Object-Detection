'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_SGIS_blended_overlay'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLX,'GLX_SGIS_blended_overlay',error_checker=_errors._error_checker)
GLX_BLENDED_RGBA_SGIS=_C('GLX_BLENDED_RGBA_SGIS',0x8025)

