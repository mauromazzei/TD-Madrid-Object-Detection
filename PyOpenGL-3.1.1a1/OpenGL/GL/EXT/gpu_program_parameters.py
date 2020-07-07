'''OpenGL extension EXT.gpu_program_parameters

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.gpu_program_parameters to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a new set of procedures to load multiple 
	consecutive program environment parameters more efficiently, via a single 
	GL call instead of multiple calls.  This will reduce the amount of CPU 
	overhead involved in loading parameters. 
	
	With the existing ARB_vertex_program and ARB_fragment_program APIs, 
	program parameters must be loaded one at a time, via separate calls. 
	While the NV_vertex_program extension provides a set of similar functions 
	that can be used to load program environment parameters (which are 
	equivalent to "program parameters" in NV_vertex_program), no such function 
	exists for program local parameters. 

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/gpu_program_parameters.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.gpu_program_parameters import *
from OpenGL.raw.GL.EXT.gpu_program_parameters import _EXTENSION_NAME

def glInitGpuProgramParametersEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glProgramEnvParameters4fvEXT.params size not checked against count*4
glProgramEnvParameters4fvEXT=wrapper.wrapper(glProgramEnvParameters4fvEXT).setInputArraySize(
    'params', None
)
# INPUT glProgramLocalParameters4fvEXT.params size not checked against count*4
glProgramLocalParameters4fvEXT=wrapper.wrapper(glProgramLocalParameters4fvEXT).setInputArraySize(
    'params', None
)
### END AUTOGENERATED SECTION