'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_SGIX_visual_select_group'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLX,'GLX_SGIX_visual_select_group',error_checker=_errors._error_checker)
GLX_VISUAL_SELECT_GROUP_SGIX=_C('GLX_VISUAL_SELECT_GROUP_SGIX',0x8028)

