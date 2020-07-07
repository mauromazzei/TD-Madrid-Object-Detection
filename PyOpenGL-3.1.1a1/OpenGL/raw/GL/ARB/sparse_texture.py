'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ARB_sparse_texture'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ARB_sparse_texture',error_checker=_errors._error_checker)
GL_MAX_SPARSE_3D_TEXTURE_SIZE_ARB=_C('GL_MAX_SPARSE_3D_TEXTURE_SIZE_ARB',0x9199)
GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_ARB=_C('GL_MAX_SPARSE_ARRAY_TEXTURE_LAYERS_ARB',0x919A)
GL_MAX_SPARSE_TEXTURE_SIZE_ARB=_C('GL_MAX_SPARSE_TEXTURE_SIZE_ARB',0x9198)
GL_NUM_SPARSE_LEVELS_ARB=_C('GL_NUM_SPARSE_LEVELS_ARB',0x91AA)
GL_NUM_VIRTUAL_PAGE_SIZES_ARB=_C('GL_NUM_VIRTUAL_PAGE_SIZES_ARB',0x91A8)
GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_ARB=_C('GL_SPARSE_TEXTURE_FULL_ARRAY_CUBE_MIPMAPS_ARB',0x91A9)
GL_TEXTURE_SPARSE_ARB=_C('GL_TEXTURE_SPARSE_ARB',0x91A6)
GL_VIRTUAL_PAGE_SIZE_INDEX_ARB=_C('GL_VIRTUAL_PAGE_SIZE_INDEX_ARB',0x91A7)
GL_VIRTUAL_PAGE_SIZE_X_ARB=_C('GL_VIRTUAL_PAGE_SIZE_X_ARB',0x9195)
GL_VIRTUAL_PAGE_SIZE_Y_ARB=_C('GL_VIRTUAL_PAGE_SIZE_Y_ARB',0x9196)
GL_VIRTUAL_PAGE_SIZE_Z_ARB=_C('GL_VIRTUAL_PAGE_SIZE_Z_ARB',0x9197)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTexPageCommitmentARB(target,level,xoffset,yoffset,zoffset,width,height,depth,resident):pass
