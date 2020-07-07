'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLX import _types as _cs
# End users want this...
from OpenGL.raw.GLX._types import *
from OpenGL.raw.GLX import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLX_EXT_import_context'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLX,'GLX_EXT_import_context',error_checker=_errors._error_checker)
GLX_SCREEN_EXT=_C('GLX_SCREEN_EXT',0x800C)
GLX_SHARE_CONTEXT_EXT=_C('GLX_SHARE_CONTEXT_EXT',0x800A)
GLX_VISUAL_ID_EXT=_C('GLX_VISUAL_ID_EXT',0x800B)
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXContext)
def glXFreeContextEXT(dpy,context):pass
@_f
@_p.types(_cs.GLXContextID,_cs.GLXContext)
def glXGetContextIDEXT(context):pass
@_f
@_p.types(ctypes.POINTER(_cs.Display),)
def glXGetCurrentDisplayEXT():pass
@_f
@_p.types(_cs.GLXContext,ctypes.POINTER(_cs.Display),_cs.GLXContextID)
def glXImportContextEXT(dpy,contextID):pass
@_f
@_p.types(_cs.c_int,ctypes.POINTER(_cs.Display),_cs.GLXContext,_cs.c_int,ctypes.POINTER(_cs.c_int))
def glXQueryContextInfoEXT(dpy,context,attribute,value):pass
