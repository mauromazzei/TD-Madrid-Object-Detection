'''OpenGL extension AMD.occlusion_query_event

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.occlusion_query_event to provide a more 
Python-friendly API

Overview (from the spec)
	
	Occlusion queries provide a means to count the number of fragments that
	pass the depth and stencil tests and that may contribute to a rendered
	image. In unextended OpenGL, an occlusion query increments its
	samples-passed count whenever a sample passes both the stencil test and
	the depth test (if enabled). However, there is no way to count fragments
	that fail the stencil test, or pass the stencil test and then subsequently
	fail the depth test.
	
	This extension introduces the concept of occlusion query events and changes
	the concept of an occlusion query from counting passed fragments to counting
	fragments that generate any of a user-selectable set of events. Provided
	events include passing the depth test, and passing or failing the stencil
	test. For a given occlusion query object, counting of these events may be
	enabled or disabled, allowing any combination to be counted.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/occlusion_query_event.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.AMD.occlusion_query_event import *
from OpenGL.raw.GL.AMD.occlusion_query_event import _EXTENSION_NAME

def glInitOcclusionQueryEventAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION