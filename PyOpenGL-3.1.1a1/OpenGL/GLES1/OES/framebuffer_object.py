'''OpenGL extension OES.framebuffer_object

This module customises the behaviour of the 
OpenGL.raw.GLES1.OES.framebuffer_object to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/framebuffer_object.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES1 import _types, _glgets
from OpenGL.raw.GLES1.OES.framebuffer_object import *
from OpenGL.raw.GLES1.OES.framebuffer_object import _EXTENSION_NAME

def glInitFramebufferObjectOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glDeleteRenderbuffersOES.renderbuffers size not checked against n
glDeleteRenderbuffersOES=wrapper.wrapper(glDeleteRenderbuffersOES).setInputArraySize(
    'renderbuffers', None
)
# INPUT glGenRenderbuffersOES.renderbuffers size not checked against n
glGenRenderbuffersOES=wrapper.wrapper(glGenRenderbuffersOES).setInputArraySize(
    'renderbuffers', None
)
# INPUT glGetRenderbufferParameterivOES.params size not checked against 'pname'
glGetRenderbufferParameterivOES=wrapper.wrapper(glGetRenderbufferParameterivOES).setInputArraySize(
    'params', None
)
# INPUT glDeleteFramebuffersOES.framebuffers size not checked against n
glDeleteFramebuffersOES=wrapper.wrapper(glDeleteFramebuffersOES).setInputArraySize(
    'framebuffers', None
)
# INPUT glGenFramebuffersOES.framebuffers size not checked against n
glGenFramebuffersOES=wrapper.wrapper(glGenFramebuffersOES).setInputArraySize(
    'framebuffers', None
)
# INPUT glGetFramebufferAttachmentParameterivOES.params size not checked against 'pname'
glGetFramebufferAttachmentParameterivOES=wrapper.wrapper(glGetFramebufferAttachmentParameterivOES).setInputArraySize(
    'params', None
)
### END AUTOGENERATED SECTION