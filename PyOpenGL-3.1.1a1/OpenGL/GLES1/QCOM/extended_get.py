'''OpenGL extension QCOM.extended_get

This module customises the behaviour of the 
OpenGL.raw.GLES1.QCOM.extended_get to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/QCOM/extended_get.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.QCOM.extended_get import *
from OpenGL.raw.GLES1.QCOM.extended_get import _EXTENSION_NAME

def glInitExtendedGetQCOM():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glExtGetBuffersQCOM.buffers size not checked against maxBuffers
glExtGetBuffersQCOM=wrapper.wrapper(glExtGetBuffersQCOM).setInputArraySize(
    'buffers', None
).setInputArraySize(
    'numBuffers', 1
)
# INPUT glExtGetRenderbuffersQCOM.renderbuffers size not checked against maxRenderbuffers
glExtGetRenderbuffersQCOM=wrapper.wrapper(glExtGetRenderbuffersQCOM).setInputArraySize(
    'numRenderbuffers', 1
).setInputArraySize(
    'renderbuffers', None
)
# INPUT glExtGetFramebuffersQCOM.framebuffers size not checked against maxFramebuffers
glExtGetFramebuffersQCOM=wrapper.wrapper(glExtGetFramebuffersQCOM).setInputArraySize(
    'framebuffers', None
).setInputArraySize(
    'numFramebuffers', 1
)
### END AUTOGENERATED SECTION