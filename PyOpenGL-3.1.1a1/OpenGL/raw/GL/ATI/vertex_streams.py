'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_ATI_vertex_streams'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_ATI_vertex_streams',error_checker=_errors._error_checker)
GL_MAX_VERTEX_STREAMS_ATI=_C('GL_MAX_VERTEX_STREAMS_ATI',0x876B)
GL_VERTEX_SOURCE_ATI=_C('GL_VERTEX_SOURCE_ATI',0x8774)
GL_VERTEX_STREAM0_ATI=_C('GL_VERTEX_STREAM0_ATI',0x876C)
GL_VERTEX_STREAM1_ATI=_C('GL_VERTEX_STREAM1_ATI',0x876D)
GL_VERTEX_STREAM2_ATI=_C('GL_VERTEX_STREAM2_ATI',0x876E)
GL_VERTEX_STREAM3_ATI=_C('GL_VERTEX_STREAM3_ATI',0x876F)
GL_VERTEX_STREAM4_ATI=_C('GL_VERTEX_STREAM4_ATI',0x8770)
GL_VERTEX_STREAM5_ATI=_C('GL_VERTEX_STREAM5_ATI',0x8771)
GL_VERTEX_STREAM6_ATI=_C('GL_VERTEX_STREAM6_ATI',0x8772)
GL_VERTEX_STREAM7_ATI=_C('GL_VERTEX_STREAM7_ATI',0x8773)
@_f
@_p.types(None,_cs.GLenum)
def glClientActiveVertexStreamATI(stream):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLbyte,_cs.GLbyte,_cs.GLbyte)
def glNormalStream3bATI(stream,nx,ny,nz):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLbyteArray)
def glNormalStream3bvATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glNormalStream3dATI(stream,nx,ny,nz):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glNormalStream3dvATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glNormalStream3fATI(stream,nx,ny,nz):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glNormalStream3fvATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint)
def glNormalStream3iATI(stream,nx,ny,nz):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glNormalStream3ivATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glNormalStream3sATI(stream,nx,ny,nz):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLshortArray)
def glNormalStream3svATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glVertexBlendEnvfATI(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glVertexBlendEnviATI(pname,param):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble)
def glVertexStream1dATI(stream,x):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glVertexStream1dvATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat)
def glVertexStream1fATI(stream,x):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glVertexStream1fvATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glVertexStream1iATI(stream,x):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glVertexStream1ivATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLshort)
def glVertexStream1sATI(stream,x):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLshortArray)
def glVertexStream1svATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble)
def glVertexStream2dATI(stream,x,y):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glVertexStream2dvATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat)
def glVertexStream2fATI(stream,x,y):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glVertexStream2fvATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint)
def glVertexStream2iATI(stream,x,y):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glVertexStream2ivATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLshort,_cs.GLshort)
def glVertexStream2sATI(stream,x,y):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLshortArray)
def glVertexStream2svATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glVertexStream3dATI(stream,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glVertexStream3dvATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glVertexStream3fATI(stream,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glVertexStream3fvATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint)
def glVertexStream3iATI(stream,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glVertexStream3ivATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glVertexStream3sATI(stream,x,y,z):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLshortArray)
def glVertexStream3svATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glVertexStream4dATI(stream,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLdoubleArray)
def glVertexStream4dvATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glVertexStream4fATI(stream,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLfloatArray)
def glVertexStream4fvATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glVertexStream4iATI(stream,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray)
def glVertexStream4ivATI(stream,coords):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLshort,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glVertexStream4sATI(stream,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLshortArray)
def glVertexStream4svATI(stream,coords):pass
