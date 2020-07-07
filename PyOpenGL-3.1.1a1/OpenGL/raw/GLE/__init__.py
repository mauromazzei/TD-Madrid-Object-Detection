# -*- coding: iso-8859-1 -*-
"""Raw (C-style) API for OpenGL.GLE

Automatically generated by the generateraw script, do not edit!
"""
from OpenGL.raw.GLE.constants import *

from ctypes import *
from OpenGL import platform, arrays
from OpenGL.constant import Constant
from OpenGL.raw.GL import _types as GL_types
GLvoid = GL_types.GLvoid




gleDouble = c_double
gleAffine = gleDouble * 3 * 2


# /usr/include/GL/gle.h 136
gleExtrusion = platform.createBaseFunction( 
    'gleExtrusion', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[c_int,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray,c_int,arrays.GLdoubleArray,arrays.GLfloatArray],
    doc='gleExtrusion( c_int(ncp), arrays.GLdoubleArray(contour), arrays.GLdoubleArray(cont_normal), arrays.GLdoubleArray(up), c_int(npoints), arrays.GLdoubleArray(point_array), arrays.GLfloatArray(color_array) ) -> None', 
    argNames=('ncp', 'contour', 'cont_normal', 'up', 'npoints', 'point_array', 'color_array'),
)


# /usr/include/GL/gle.h 110
gleGetJoinStyle = platform.createBaseFunction( 
    'gleGetJoinStyle', dll=platform.PLATFORM.GLE, resultType=c_int, 
    argTypes=[],
    doc='gleGetJoinStyle(  ) -> c_int', 
    argNames=(),
)


# /usr/include/GL/gle.h 114
gleGetNumSides = platform.createBaseFunction( 
    'gleGetNumSides', dll=platform.PLATFORM.GLE, resultType=c_int, 
    argTypes=[],
    doc='gleGetNumSides(  ) -> c_int', 
    argNames=(),
)


# /usr/include/GL/gle.h 195
gleHelicoid = platform.createBaseFunction( 
    'gleHelicoid', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[gleDouble,gleDouble,gleDouble,gleDouble,gleDouble,arrays.GLdoubleArray,arrays.GLdoubleArray,gleDouble,gleDouble],
    doc='gleHelicoid( gleDouble(rToroid), gleDouble(startRadius), gleDouble(drdTheta), gleDouble(startZ), gleDouble(dzdTheta), arrays.GLdoubleArray(startXform), arrays.GLdoubleArray(dXformdTheta), gleDouble(startTheta), gleDouble(sweepTheta) ) -> None', 
    argNames=('rToroid', 'startRadius', 'drdTheta', 'startZ', 'dzdTheta', 'startXform', 'dXformdTheta', 'startTheta', 'sweepTheta'),
)


# /usr/include/GL/gle.h 184
gleLathe = platform.createBaseFunction( 
    'gleLathe', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[c_int,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray,gleDouble,gleDouble,gleDouble,gleDouble,arrays.GLdoubleArray,arrays.GLdoubleArray,gleDouble,gleDouble],
    doc='gleLathe( c_int(ncp), arrays.GLdoubleArray(contour), arrays.GLdoubleArray(cont_normal), arrays.GLdoubleArray(up), gleDouble(startRadius), gleDouble(drdTheta), gleDouble(startZ), gleDouble(dzdTheta), arrays.GLdoubleArray(startXform), arrays.GLdoubleArray(dXformdTheta), gleDouble(startTheta), gleDouble(sweepTheta) ) -> None', 
    argNames=('ncp', 'contour', 'cont_normal', 'up', 'startRadius', 'drdTheta', 'startZ', 'dzdTheta', 'startXform', 'dXformdTheta', 'startTheta', 'sweepTheta'),
)


# /usr/include/GL/gle.h 127
glePolyCone = platform.createBaseFunction( 
    'glePolyCone', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[c_int,arrays.GLdoubleArray,arrays.GLfloatArray,arrays.GLdoubleArray],
    doc='glePolyCone( c_int(npoints), arrays.GLdoubleArray(point_array), arrays.GLfloatArray(color_array), arrays.GLdoubleArray(radius_array) ) -> None', 
    argNames=('npoints', 'point_array', 'color_array', 'radius_array'),
)


# /usr/include/GL/gle.h 121
glePolyCylinder = platform.createBaseFunction( 
    'glePolyCylinder', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[c_int,arrays.GLdoubleArray,arrays.GLfloatArray,gleDouble],
    doc='glePolyCylinder( c_int(npoints), arrays.GLdoubleArray(point_array), arrays.GLfloatArray(color_array), gleDouble(radius) ) -> None', 
    argNames=('npoints', 'point_array', 'color_array', 'radius'),
)


# /usr/include/GL/gle.h 215
gleScrew = platform.createBaseFunction( 
    'gleScrew', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[c_int,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray,gleDouble,gleDouble,gleDouble],
    doc='gleScrew( c_int(ncp), arrays.GLdoubleArray(contour), arrays.GLdoubleArray(cont_normal), arrays.GLdoubleArray(up), gleDouble(startz), gleDouble(endz), gleDouble(twist) ) -> None', 
    argNames=('ncp', 'contour', 'cont_normal', 'up', 'startz', 'endz', 'twist'),
)

# /usr/include/GL/gle.h 111
gleSetJoinStyle = platform.createBaseFunction( 
    'gleSetJoinStyle', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[c_int],
    doc='gleSetJoinStyle( c_int(style) ) -> None', 
    argNames=('style',),
)


# /usr/include/GL/gle.h 115
gleSetNumSides = platform.createBaseFunction( 
    'gleSetNumSides', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[c_int],
    doc='gleSetNumSides( c_int(slices) ) -> None', 
    argNames=('slices',),
)


# /usr/include/GL/gle.h 170
gleSpiral = platform.createBaseFunction( 
    'gleSpiral', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[c_int,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray,gleDouble,gleDouble,gleDouble,gleDouble,arrays.GLdoubleArray,arrays.GLdoubleArray,gleDouble,gleDouble],
    doc='gleSpiral( c_int(ncp), arrays.GLdoubleArray(contour), arrays.GLdoubleArray(cont_normal), arrays.GLdoubleArray(up), gleDouble(startRadius), gleDouble(drdTheta), gleDouble(startZ), gleDouble(dzdTheta), arrays.GLdoubleArray(startXform), arrays.GLdoubleArray(dXformdTheta), gleDouble(startTheta), gleDouble(sweepTheta) ) -> None', 
    argNames=('ncp', 'contour', 'cont_normal', 'up', 'startRadius', 'drdTheta', 'startZ', 'dzdTheta', 'startXform', 'dXformdTheta', 'startTheta', 'sweepTheta'),
)


# /usr/include/GL/gle.h 156
gleSuperExtrusion = platform.createBaseFunction( 
    'gleSuperExtrusion', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[c_int,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray,c_int,arrays.GLdoubleArray,arrays.GLfloatArray,arrays.GLdoubleArray],
    doc='gleSuperExtrusion( c_int(ncp), arrays.GLdoubleArray(contour), arrays.GLdoubleArray(cont_normal), arrays.GLdoubleArray(up), c_int(npoints), arrays.GLdoubleArray(point_array), arrays.GLfloatArray(color_array), arrays.GLdoubleArray(xform_array) ) -> None', 
    argNames=('ncp', 'contour', 'cont_normal', 'up', 'npoints', 'point_array', 'color_array', 'xform_array'),
)


# /usr/include/GL/gle.h 217
gleTextureMode = platform.createBaseFunction( 
    'gleTextureMode', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[c_int],
    doc='gleTextureMode( c_int(mode) ) -> None', 
    argNames=('mode',),
)


# /usr/include/GL/gle.h 206
gleToroid = platform.createBaseFunction( 
    'gleToroid', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[gleDouble,gleDouble,gleDouble,gleDouble,gleDouble,arrays.GLdoubleArray,arrays.GLdoubleArray,gleDouble,gleDouble],
    doc='gleToroid( gleDouble(rToroid), gleDouble(startRadius), gleDouble(drdTheta), gleDouble(startZ), gleDouble(dzdTheta), arrays.GLdoubleArray(startXform), arrays.GLdoubleArray(dXformdTheta), gleDouble(startTheta), gleDouble(sweepTheta) ) -> None', 
    argNames=('rToroid', 'startRadius', 'drdTheta', 'startZ', 'dzdTheta', 'startXform', 'dXformdTheta', 'startTheta', 'sweepTheta'),
)


# /usr/include/GL/gle.h 146
gleTwistExtrusion = platform.createBaseFunction( 
    'gleTwistExtrusion', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[c_int,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray,c_int,arrays.GLdoubleArray,arrays.GLfloatArray,arrays.GLdoubleArray],
    doc='gleTwistExtrusion( c_int(ncp), arrays.GLdoubleArray(contour), arrays.GLdoubleArray(cont_normal), arrays.GLdoubleArray(up), c_int(npoints), arrays.GLdoubleArray(point_array), arrays.GLfloatArray(color_array), arrays.GLdoubleArray(twist_array) ) -> None', 
    argNames=('ncp', 'contour', 'cont_normal', 'up', 'npoints', 'point_array', 'color_array', 'twist_array'),
)


# /usr/include/GL/gle.h 221
rot_about_axis = platform.createBaseFunction( 
    'rot_about_axis', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[gleDouble,arrays.GLdoubleArray],
    doc='rot_about_axis( gleDouble(angle), arrays.GLdoubleArray(axis) ) -> None', 
    argNames=('angle', 'axis'),
)


# /usr/include/GL/gle.h 220
rot_axis = platform.createBaseFunction( 
    'rot_axis', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[gleDouble,arrays.GLdoubleArray],
    doc='rot_axis( gleDouble(omega), arrays.GLdoubleArray(axis) ) -> None', 
    argNames=('omega', 'axis'),
)


# /usr/include/GL/gle.h 222
rot_omega = platform.createBaseFunction( 
    'rot_omega', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[arrays.GLdoubleArray],
    doc='rot_omega( arrays.GLdoubleArray(axis) ) -> None', 
    argNames=('axis',),
)


# /usr/include/GL/gle.h 223
rot_prince = platform.createBaseFunction( 
    'rot_prince', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[gleDouble,c_char],
    doc='rot_prince( gleDouble(omega), c_char(axis) ) -> None', 
    argNames=('omega', 'axis'),
)


# /usr/include/GL/gle.h 225
urot_about_axis = platform.createBaseFunction( 
    'urot_about_axis', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[arrays.GLdoubleArray,gleDouble,arrays.GLdoubleArray],
    doc='urot_about_axis( arrays.GLdoubleArray(m), gleDouble(angle), arrays.GLdoubleArray(axis) ) -> None', 
    argNames=('m', 'angle', 'axis'),
)


# /usr/include/GL/gle.h 224
urot_axis = platform.createBaseFunction( 
    'urot_axis', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[arrays.GLdoubleArray,gleDouble,arrays.GLdoubleArray],
    doc='urot_axis( arrays.GLdoubleArray(m), gleDouble(omega), arrays.GLdoubleArray(axis) ) -> None', 
    argNames=('m', 'omega', 'axis'),
)


# /usr/include/GL/gle.h 226
urot_omega = platform.createBaseFunction( 
    'urot_omega', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[arrays.GLdoubleArray,arrays.GLdoubleArray],
    doc='urot_omega( arrays.GLdoubleArray(m), arrays.GLdoubleArray(axis) ) -> None', 
    argNames=('m', 'axis'),
)


# /usr/include/GL/gle.h 227
urot_prince = platform.createBaseFunction( 
    'urot_prince', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[arrays.GLdoubleArray,gleDouble,c_char],
    doc='urot_prince( arrays.GLdoubleArray(m), gleDouble(omega), c_char(axis) ) -> None', 
    argNames=('m', 'omega', 'axis'),
)


# /usr/include/GL/gle.h 232
uview_direction = platform.createBaseFunction( 
    'uview_direction', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray],
    doc='uview_direction( arrays.GLdoubleArray(m), arrays.GLdoubleArray(v21), arrays.GLdoubleArray(up) ) -> None', 
    argNames=('m', 'v21', 'up'),
)


# /usr/include/GL/gle.h 237
uviewpoint = platform.createBaseFunction( 
    'uviewpoint', dll=platform.PLATFORM.GLE, resultType=None, 
    argTypes=[arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray,arrays.GLdoubleArray],
    doc='uviewpoint( arrays.GLdoubleArray(m), arrays.GLdoubleArray(v1), arrays.GLdoubleArray(v2), arrays.GLdoubleArray(up) ) -> None', 
    argNames=('m', 'v1', 'v2', 'up'),
)

__all__ = [
    'GLE_TEXTURE_ENABLE',
    'GLE_TEXTURE_NORMAL_CYL',
    'GLE_TEXTURE_NORMAL_FLAT',
    'GLE_TEXTURE_NORMAL_MODEL_CYL',
    'GLE_TEXTURE_NORMAL_MODEL_FLAT',
    'GLE_TEXTURE_NORMAL_MODEL_SPH',
    'GLE_TEXTURE_NORMAL_SPH',
    'GLE_TEXTURE_STYLE_MASK',
    'GLE_TEXTURE_VERTEX_CYL',
    'GLE_TEXTURE_VERTEX_FLAT',
    'GLE_TEXTURE_VERTEX_MODEL_CYL',
    'GLE_TEXTURE_VERTEX_MODEL_FLAT',
    'GLE_TEXTURE_VERTEX_MODEL_SPH',
    'GLE_TEXTURE_VERTEX_SPH',
    'TUBE_CONTOUR_CLOSED',
    'TUBE_JN_ANGLE',
    'TUBE_JN_CAP',
    'TUBE_JN_CUT',
    'TUBE_JN_MASK',
    'TUBE_JN_RAW',
    'TUBE_JN_ROUND',
    'TUBE_NORM_EDGE',
    'TUBE_NORM_FACET',
    'TUBE_NORM_MASK',
    'TUBE_NORM_PATH_EDGE',
    '__GLE_DOUBLE',
    'gleAffine',
    'gleDouble',
    'gleExtrusion',
    'gleGetJoinStyle',
    'gleGetNumSides',
    'gleHelicoid',
    'gleLathe',
    'glePolyCone',
    'glePolyCylinder',
    'gleScrew',
    'gleSetJoinStyle',
    'gleSetNumSides',
    'gleSpiral',
    'gleSuperExtrusion',
    'gleTextureMode',
    'gleToroid',
    'gleTwistExtrusion',
    'rot_about_axis',
    'rot_axis',
    'rot_omega',
    'rot_prince',
    'urot_about_axis',
    'urot_axis',
    'urot_omega',
    'urot_prince',
    'uview_direction',
    'uviewpoint'
]
