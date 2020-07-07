'''OpenGL extension ARB.fragment_program

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.fragment_program to provide a more 
Python-friendly API

Overview (from the spec)
	
	Unextended OpenGL mandates a certain set of configurable per-
	fragment computations defining texture application, texture 
	environment, color sum, and fog operations.  Several extensions have 
	added further per-fragment computations to OpenGL.  For example, 
	extensions have defined new texture environment capabilities 
	(ARB_texture_env_add, ARB_texture_env_combine, ARB_texture_env_dot3,
	ARB_texture_env_crossbar), per-fragment depth comparisons 
	(ARB_depth_texture, ARB_shadow, ARB_shadow_ambient, 
	EXT_shadow_funcs), per-fragment lighting (EXT_fragment_lighting, 
	EXT_light_texture), and environment mapped bump mapping 
	(ATI_envmap_bumpmap).  
	
	Each such extension adds a small set of relatively inflexible per-
	fragment computations.
	
	This inflexibility is in contrast to the typical flexibility 
	provided by the underlying programmable floating point engines 
	(whether micro-coded fragment engines, DSPs, or CPUs) that are 
	traditionally used to implement OpenGL's texturing computations.  
	The purpose of this extension is to expose to the OpenGL application 
	writer a significant degree of per-fragment programmability for 
	computing fragment parameters.
	
	For the purposes of discussing this extension, a fragment program is 
	a sequence of floating-point 4-component vector operations that 
	determines how a set of program parameters (not specific to an
	individual fragment) and an input set of per-fragment parameters are 
	transformed to a set of per-fragment result parameters.
	
	The per-fragment computations for standard OpenGL given a particular 
	set of texture and fog application modes (along with any state for 
	extensions defining per-fragment computations) is, in essence, a 
	fragment program.  However, the sequence of operations is defined 
	implicitly by the current OpenGL state settings rather than defined 
	explicitly as a sequence of instructions.
	
	This extension provides an explicit mechanism for defining fragment 
	program instruction sequences for application-defined fragment 
	programs.  In order to define such fragment programs, this extension 
	defines a fragment programming model including a floating-point
	4-component vector instruction set and a relatively large set of 
	floating-point 4-component registers.
	
	The extension's fragment programming model is designed for efficient
	hardware implementation and to support a wide variety of fragment 
	programs.  By design, the entire set of existing fragment programs 
	defined by existing OpenGL per-fragment computation extensions can 
	be implemented using the extension's fragment programming model.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/fragment_program.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.fragment_program import *
from OpenGL.raw.GL.ARB.fragment_program import _EXTENSION_NAME

def glInitFragmentProgramARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glProgramStringARB.string size not checked against len
glProgramStringARB=wrapper.wrapper(glProgramStringARB).setInputArraySize(
    'string', None
)
# INPUT glDeleteProgramsARB.programs size not checked against n
glDeleteProgramsARB=wrapper.wrapper(glDeleteProgramsARB).setInputArraySize(
    'programs', None
)
glGenProgramsARB=wrapper.wrapper(glGenProgramsARB).setOutput(
    'programs',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
glProgramEnvParameter4dvARB=wrapper.wrapper(glProgramEnvParameter4dvARB).setInputArraySize(
    'params', 4
)
glProgramEnvParameter4fvARB=wrapper.wrapper(glProgramEnvParameter4fvARB).setInputArraySize(
    'params', 4
)
glProgramLocalParameter4dvARB=wrapper.wrapper(glProgramLocalParameter4dvARB).setInputArraySize(
    'params', 4
)
glProgramLocalParameter4fvARB=wrapper.wrapper(glProgramLocalParameter4fvARB).setInputArraySize(
    'params', 4
)
glGetProgramEnvParameterdvARB=wrapper.wrapper(glGetProgramEnvParameterdvARB).setOutput(
    'params',size=(4,),orPassIn=True
)
glGetProgramEnvParameterfvARB=wrapper.wrapper(glGetProgramEnvParameterfvARB).setOutput(
    'params',size=(4,),orPassIn=True
)
glGetProgramLocalParameterdvARB=wrapper.wrapper(glGetProgramLocalParameterdvARB).setOutput(
    'params',size=(4,),orPassIn=True
)
glGetProgramLocalParameterfvARB=wrapper.wrapper(glGetProgramLocalParameterfvARB).setOutput(
    'params',size=(4,),orPassIn=True
)
glGetProgramivARB=wrapper.wrapper(glGetProgramivARB).setOutput(
    'params',size=(1,),orPassIn=True
)
# OUTPUT glGetProgramStringARB.string COMPSIZE(target, pname) 
### END AUTOGENERATED SECTION
