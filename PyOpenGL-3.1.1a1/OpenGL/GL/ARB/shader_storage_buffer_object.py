'''OpenGL extension ARB.shader_storage_buffer_object

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shader_storage_buffer_object to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides the ability for OpenGL shaders to perform random
	access reads, writes, and atomic memory operations on variables stored in
	a buffer object.  Application shader code can declare sets of variables
	(referred to as "buffer variables") arranged into interface blocks in a
	manner similar to that done with uniform blocks in OpenGL 3.1.  In both
	cases, the values of the variables declared in a given interface block are
	taken from a buffer object bound to a binding point associated with the
	block.  Buffer objects used in this extension are referred to as "shader
	storage buffers".  
	
	While the capability provided by this extension is similar to that
	provided by OpenGL 3.1 and ARB_uniform_buffer_object, there are several
	significant differences.  Most importantly, shader code is allowed to
	write to shader storage buffers, while uniform buffers are always
	read-only.  Shader storage buffers have a separate set of binding points,
	with different counts and size limits.  The maximum usable size for shader
	storage buffers is implementation-dependent, but its minimum value is
	substantially larger than the minimum for uniform buffers.  
	
	The ability to write to buffer objects creates the potential for multiple
	independent shader invocations to read and write the same underlying
	memory.  The same issue exists with the ARB_shader_image_load_store
	extension provided in OpenGL 4.2, which can write to texture objects and
	buffers.  In both cases, the specification makes few guarantees related to
	the relative order of memory reads and writes performed by the shader
	invocations.  For ARB_shader_image_load_store, the OpenGL API and shading
	language do provide some control over memory transactions; those
	mechanisms also affect reads and writes of shader storage buffers.  In the
	OpenGL API, the glMemoryBarrier() call can be used to ensure that certain
	memory operations related to commands issued prior the barrier complete
	before other operations related to commands issued after the barrier.
	Additionally, the shading language provides the memoryBarrier() function
	to control the relative order of memory accesses within individual shader
	invocations and provides various memory qualifiers controlling how the
	memory corresponding to individual variables is accessed.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/shader_storage_buffer_object.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.shader_storage_buffer_object import *
from OpenGL.raw.GL.ARB.shader_storage_buffer_object import _EXTENSION_NAME

def glInitShaderStorageBufferObjectARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION