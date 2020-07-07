'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.WGL import _types as _cs
# End users want this...
from OpenGL.raw.WGL._types import *
from OpenGL.raw.WGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'WGL_ARB_make_current_read'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.WGL,'WGL_ARB_make_current_read',error_checker=_errors._error_checker)
ERROR_INCOMPATIBLE_DEVICE_CONTEXTS_ARB=_C('ERROR_INCOMPATIBLE_DEVICE_CONTEXTS_ARB',0x2054)
ERROR_INVALID_PIXEL_TYPE_ARB=_C('ERROR_INVALID_PIXEL_TYPE_ARB',0x2043)
@_f
@_p.types(_cs.HDC,)
def wglGetCurrentReadDCARB():pass
@_f
@_p.types(_cs.BOOL,_cs.HDC,_cs.HDC,_cs.HGLRC)
def wglMakeContextCurrentARB(hDrawDC,hReadDC,hglrc):pass
