'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.raw.EGL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'EGL_TIZEN_image_native_surface'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.EGL,'EGL_TIZEN_image_native_surface',error_checker=_errors._error_checker)
EGL_NATIVE_SURFACE_TIZEN=_C('EGL_NATIVE_SURFACE_TIZEN',0x32A1)

