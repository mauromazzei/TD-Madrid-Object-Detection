'''OpenGL extension ARB.vertex_buffer_object

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.vertex_buffer_object to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension defines an interface that allows various types of data
	(especially vertex array data) to be cached in high-performance
	graphics memory on the server, thereby increasing the rate of data
	transfers.
	
	Chunks of data are encapsulated within "buffer objects", which
	conceptually are nothing more than arrays of bytes, just like any
	chunk of memory.  An API is provided whereby applications can read
	from or write to buffers, either via the GL itself (glBufferData,
	glBufferSubData, glGetBufferSubData) or via a pointer to the memory.
	
	The latter technique is known as "mapping" a buffer.  When an
	application maps a buffer, it is given a pointer to the memory.  When
	the application finishes reading from or writing to the memory, it is
	required to "unmap" the buffer before it is once again permitted to
	use that buffer as a GL data source or sink.  Mapping often allows
	applications to eliminate an extra data copy otherwise required to
	access the buffer, thereby enhancing performance.  In addition,
	requiring that applications unmap the buffer to use it as a data
	source or sink ensures that certain classes of latent synchronization
	bugs cannot occur.
	
	Although this extension only defines hooks for buffer objects to be
	used with OpenGL's vertex array APIs, the API defined in this
	extension permits buffer objects to be used as either data sources or
	sinks for any GL command that takes a pointer as an argument.
	Normally, in the absence of this extension, a pointer passed into the
	GL is simply a pointer to the user's data.  This extension defines
	a mechanism whereby this pointer is used not as a pointer to the data
	itself, but as an offset into a currently bound buffer object.  The
	buffer object ID zero is reserved, and when buffer object zero is
	bound to a given target, the commands affected by that buffer binding
	behave normally.  When a nonzero buffer ID is bound, then the pointer
	represents an offset.
	
	In the case of vertex arrays, this extension defines not merely one
	binding for all attributes, but a separate binding for each
	individual attribute.  As a result, applications can source their
	attributes from multiple buffers.  An application might, for example,
	have a model with constant texture coordinates and variable geometry.
	The texture coordinates might be retrieved from a buffer object with
	the usage mode "STATIC_DRAW", indicating to the GL that the
	application does not expect to update the contents of the buffer
	frequently or even at all, while the vertices might be retrieved from
	a buffer object with the usage mode "STREAM_DRAW", indicating that
	the vertices will be updated on a regular basis.
	
	In addition, a binding is defined by which applications can source
	index data (as used by DrawElements, DrawRangeElements, and
	MultiDrawElements) from a buffer object.  On some platforms, this
	enables very large models to be rendered with no more than a few
	small commands to the graphics device.
	
	It is expected that a future extension will allow sourcing pixel data
	from and writing pixel data to a buffer object.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/vertex_buffer_object.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.vertex_buffer_object import *
from OpenGL.raw.GL.ARB.vertex_buffer_object import _EXTENSION_NAME

def glInitVertexBufferObjectARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glDeleteBuffersARB.buffers size not checked against n
glDeleteBuffersARB=wrapper.wrapper(glDeleteBuffersARB).setInputArraySize(
    'buffers', None
)
glGenBuffersARB=wrapper.wrapper(glGenBuffersARB).setOutput(
    'buffers',size=lambda x:(x,),pnameArg='n',orPassIn=True
)
# INPUT glBufferDataARB.data size not checked against size
glBufferDataARB=wrapper.wrapper(glBufferDataARB).setInputArraySize(
    'data', None
)
# INPUT glBufferSubDataARB.data size not checked against size
glBufferSubDataARB=wrapper.wrapper(glBufferSubDataARB).setInputArraySize(
    'data', None
)
glGetBufferSubDataARB=wrapper.wrapper(glGetBufferSubDataARB).setOutput(
    'data',size=lambda x:(x,),pnameArg='size',orPassIn=True
)
glGetBufferParameterivARB=wrapper.wrapper(glGetBufferParameterivARB).setOutput(
    'params',size=_glgets._glget_size_mapping,pnameArg='pname',orPassIn=True
)
glGetBufferPointervARB=wrapper.wrapper(glGetBufferPointervARB).setOutput(
    'params',size=(1,),orPassIn=True
)
### END AUTOGENERATED SECTION
from OpenGL.lazywrapper import lazy as _lazy
from OpenGL.arrays import ArrayDatatype
from OpenGL._bytes import long,integer_types

@_lazy( glBufferDataARB )
def glBufferDataARB( baseOperation, target, size, data=None, usage=None ):
    """Copy given data into the currently bound vertex-buffer-data object
    
    target -- the symbolic constant indicating which buffer type is intended
    size -- if provided, the count-in-bytes of the array
    data -- data-pointer to be used, may be None to initialize without 
        copying over a data-set 
    usage -- hint to the driver as to how to set up access to the buffer 
    
    Note: parameter "size" can be omitted, which makes the signature
        glBufferData( target, data, usage )
    instead of:
        glBufferData( target, size, data, usage )
    """
    if usage is None:
        usage = data 
        data = size 
        size = None 
    data = ArrayDatatype.asArray( data )
    if size is None:
        size = ArrayDatatype.arrayByteCount( data )
    return baseOperation( target, size, data, usage )

@_lazy( glBufferSubDataARB )
def glBufferSubDataARB( baseOperation, target, offset, size=None, data=None ):
    """Copy subset of data into the currently bound vertex-buffer-data object

    target -- the symbolic constant indicating which buffer type is intended
    offset -- offset from beginning of buffer at which to copy bytes
    size -- the count-in-bytes of the array (if an int/long), if None,
        calculate size from data, if an array and data is None, use as
        data (i.e. the parameter can be omitted and calculated)
    data -- data-pointer to be used, may be None to initialize without
        copying over a data-set

    Note that if size is not an int/long it is considered to be data
    *iff* data is None
    """
    if size is None:
        if data is None:
            raise TypeError( "Need data or size" )
    elif (not isinstance( size, integer_types)) and (data is None):
        data = size 
        size = None
    try:
        if size is not None:
            size = int( size )
    except TypeError as err:
        if data is not None:
            raise TypeError(
                """Expect an integer size *or* a data-array, not both"""
            )
        data = size 
        size = None 
    data = ArrayDatatype.asArray( data )
    if size is None:
        size = ArrayDatatype.arrayByteCount( data )
    return baseOperation( target, offset, size, data )
