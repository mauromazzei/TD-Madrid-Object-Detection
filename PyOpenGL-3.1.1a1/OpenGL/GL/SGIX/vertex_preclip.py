'''OpenGL extension SGIX.vertex_preclip

This module customises the behaviour of the 
OpenGL.raw.GL.SGIX.vertex_preclip to provide a more 
Python-friendly API

Overview (from the spec)
	
	Certain graphics subsystems are capable of performing fast
	2D viewport or, in some cases, 3D volume "scissoring" operations
	within some coordinate range much faster that the host CPU could
	re-tesselate clipped primitives.
	
	This extension introduces the notion of an extended rasterizable view
	volume that is an expansion of the clip-space view volume.	This volume
	is the space within which a particular graphics system is much more
	efficient at rejecting fragments that lie outside the view volume than
	it is at performing strict view volume clipping.
	
	Clip-checking can be turned on or off through the glEnable/glDisable
	mechanism, and can be further controlled by using glHint.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/vertex_preclip.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.SGIX.vertex_preclip import *
from OpenGL.raw.GL.SGIX.vertex_preclip import _EXTENSION_NAME

def glInitVertexPreclipSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION