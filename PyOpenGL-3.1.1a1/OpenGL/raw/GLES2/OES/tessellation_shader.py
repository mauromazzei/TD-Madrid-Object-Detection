'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_OES_tessellation_shader'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_OES_tessellation_shader',error_checker=_errors._error_checker)
GL_CCW=_C('GL_CCW',0x0901)
GL_CW=_C('GL_CW',0x0900)
GL_EQUAL=_C('GL_EQUAL',0x0202)
GL_FRACTIONAL_EVEN_OES=_C('GL_FRACTIONAL_EVEN_OES',0x8E7C)
GL_FRACTIONAL_ODD_OES=_C('GL_FRACTIONAL_ODD_OES',0x8E7B)
GL_ISOLINES_OES=_C('GL_ISOLINES_OES',0x8E7A)
GL_IS_PER_PATCH_OES=_C('GL_IS_PER_PATCH_OES',0x92E7)
GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS_OES=_C('GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS_OES',0x8E1E)
GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS_OES=_C('GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS_OES',0x8E1F)
GL_MAX_PATCH_VERTICES_OES=_C('GL_MAX_PATCH_VERTICES_OES',0x8E7D)
GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS_OES=_C('GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS_OES',0x92D3)
GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS_OES=_C('GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS_OES',0x92CD)
GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS_OES=_C('GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS_OES',0x90CB)
GL_MAX_TESS_CONTROL_INPUT_COMPONENTS_OES=_C('GL_MAX_TESS_CONTROL_INPUT_COMPONENTS_OES',0x886C)
GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS_OES=_C('GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS_OES',0x8E83)
GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS_OES=_C('GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS_OES',0x90D8)
GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS_OES=_C('GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS_OES',0x8E81)
GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS_OES=_C('GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS_OES',0x8E85)
GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS_OES=_C('GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS_OES',0x8E89)
GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS_OES=_C('GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS_OES',0x8E7F)
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS_OES=_C('GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS_OES',0x92D4)
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS_OES=_C('GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS_OES',0x92CE)
GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS_OES=_C('GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS_OES',0x90CC)
GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS_OES=_C('GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS_OES',0x886D)
GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS_OES=_C('GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS_OES',0x8E86)
GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS_OES=_C('GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS_OES',0x90D9)
GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS_OES=_C('GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS_OES',0x8E82)
GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS_OES=_C('GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS_OES',0x8E8A)
GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS_OES=_C('GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS_OES',0x8E80)
GL_MAX_TESS_GEN_LEVEL_OES=_C('GL_MAX_TESS_GEN_LEVEL_OES',0x8E7E)
GL_MAX_TESS_PATCH_COMPONENTS_OES=_C('GL_MAX_TESS_PATCH_COMPONENTS_OES',0x8E84)
GL_PATCHES_OES=_C('GL_PATCHES_OES',0x000E)
GL_PATCH_VERTICES_OES=_C('GL_PATCH_VERTICES_OES',0x8E72)
GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED_OES=_C('GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED_OES',0x8221)
GL_QUADS_OES=_C('GL_QUADS_OES',0x0007)
GL_REFERENCED_BY_TESS_CONTROL_SHADER_OES=_C('GL_REFERENCED_BY_TESS_CONTROL_SHADER_OES',0x9307)
GL_REFERENCED_BY_TESS_EVALUATION_SHADER_OES=_C('GL_REFERENCED_BY_TESS_EVALUATION_SHADER_OES',0x9308)
GL_TESS_CONTROL_OUTPUT_VERTICES_OES=_C('GL_TESS_CONTROL_OUTPUT_VERTICES_OES',0x8E75)
GL_TESS_CONTROL_SHADER_BIT_OES=_C('GL_TESS_CONTROL_SHADER_BIT_OES',0x00000008)
GL_TESS_CONTROL_SHADER_OES=_C('GL_TESS_CONTROL_SHADER_OES',0x8E88)
GL_TESS_EVALUATION_SHADER_BIT_OES=_C('GL_TESS_EVALUATION_SHADER_BIT_OES',0x00000010)
GL_TESS_EVALUATION_SHADER_OES=_C('GL_TESS_EVALUATION_SHADER_OES',0x8E87)
GL_TESS_GEN_MODE_OES=_C('GL_TESS_GEN_MODE_OES',0x8E76)
GL_TESS_GEN_POINT_MODE_OES=_C('GL_TESS_GEN_POINT_MODE_OES',0x8E79)
GL_TESS_GEN_SPACING_OES=_C('GL_TESS_GEN_SPACING_OES',0x8E77)
GL_TESS_GEN_VERTEX_ORDER_OES=_C('GL_TESS_GEN_VERTEX_ORDER_OES',0x8E78)
GL_TRIANGLES=_C('GL_TRIANGLES',0x0004)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glPatchParameteriOES(pname,value):pass
