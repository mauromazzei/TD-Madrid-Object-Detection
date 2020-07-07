'''OpenGL extension ARB.get_program_binary

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.get_program_binary to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension introduces new commands to retrieve and set the binary
	representation of a program object.  GetProgramBinary allows an
	application to cache compiled and linked programs to avoid compiling and
	linking when used again. This may even allow the GL itself to act as an
	offline compiler.  The resulting program binary can be reloaded into the
	GL via ProgramBinary.  This is a very useful path for applications that
	wish to remain portable by shipping pure GLSL source shaders, yet would
	like to avoid the cost of compiling their shaders at runtime.  Instead an
	application can supply its GLSL source shaders during first application run,
	or even during installation.  The application then compiles and links its
	shaders and reads back the program binaries.  On subsequent runs, only the
	program binaries need be supplied.
	
	ProgramBinary may also accept binaries in vendor-specific formats
	produced by specialized offline compilation tools. This extension does not 
	add any such formats, but allows for them in further extensions. Though the
	level of optimization may not be identical -- the offline shader compiler
	may have the luxury of more aggressive optimization at its disposal --
	program binaries generated online by the GL are interchangeable with those
	generated offline by an SDK tool.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/get_program_binary.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.get_program_binary import *
from OpenGL.raw.GL.ARB.get_program_binary import _EXTENSION_NAME

def glInitGetProgramBinaryARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

glGetProgramBinary=wrapper.wrapper(glGetProgramBinary).setOutput(
    'binary',size=lambda x:(x,),pnameArg='bufSize',orPassIn=True
).setOutput(
    'binaryFormat',size=(1,),orPassIn=True
).setOutput(
    'length',size=(1,),orPassIn=True
)
# INPUT glProgramBinary.binary size not checked against length
glProgramBinary=wrapper.wrapper(glProgramBinary).setInputArraySize(
    'binary', None
)
### END AUTOGENERATED SECTION