'''OpenGL extension ARB.debug_output

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.debug_output to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows the GL to notify applications when various
	events occur that may be useful during application development and
	debugging.
	
	These events are represented in the form of enumerable messages with
	a human-readable string representation.  Examples of debug events
	include incorrect use of the GL, warnings of undefined behavior, and
	performance warnings.
	
	A message is uniquely identified by a source, a type and an
	implementation-dependent ID within the source and type pair.
	
	A message's source identifies the origin of the message and can
	either describe components of the GL, the window system,
	third-party external sources such as external debuggers, or even
	the application itself.
	
	The type of the message roughly identifies the nature of the event
	that caused the message.  Examples include errors, performance
	warnings, or warnings about undefined behavior.
	
	A message's ID for a given source and type further
	distinguishes messages within those groups.  For example, an error
	caused by a negative parameter value or an invalid internal
	texture format are both errors generated by the API, but would
	likely have different message IDs.
	
	Each message is also assigned to a severity level that denotes
	roughly how "important" that message is in comparison to other
	messages across all sources and types.  For example, notification 
	of a GL error would likely have a higher severity than a performance
	warning due to redundant state changes.
	
	Finally, every message contains an implementation-dependent string
	representation that provides a useful description of the event.
	
	Messages are communicated to the application through an application-
	defined callback function that is called by the GL implementation on
	each debug message.  The motivation for the callback routine is to
	free application developers from actively having to query whether
	a GL error, or any other debuggable event has happened after each
	call to a GL function.  With a callback, developers can keep their
	code free of debug checks, and only have to react to messages as
	they occur.  In situations where using a callback is not possible,
	a message log is also provided that stores copies of recent messages
	until they are actively queried.
	
	To control the volume of debug output, messages can be disabled
	either individually by ID, or entire groups of messages can be
	turned off based on combination of source and type.
	
	The only requirement on the minimum quantity and type of messages
	that implementations of this extension must support is that some
	sort of message must be sent notifying the application whenever any
	GL error occurs.  Any further messages are left to the
	implementation.  Implementations do not have to output messages from
	all sources nor do they have to use all types of messages listed
	by this extension, and both new sources and types can be added by
	other extensions. 
	
	For performance reasons it is recommended, but not required, that
	implementations restrict supporting this extension only to
	contexts created using the debug flag as provided by
	WGL_create_context or GLX_create_context.  This extension places no
	limits on any other functionality provided by debug contexts through
	other extensions.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/debug_output.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ARB.debug_output import *
from OpenGL.raw.GL.ARB.debug_output import _EXTENSION_NAME

def glInitDebugOutputARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glDebugMessageControlARB.ids size not checked against count
glDebugMessageControlARB=wrapper.wrapper(glDebugMessageControlARB).setInputArraySize(
    'ids', None
)
# INPUT glDebugMessageInsertARB.buf size not checked against length
glDebugMessageInsertARB=wrapper.wrapper(glDebugMessageInsertARB).setInputArraySize(
    'buf', None
)
# INPUT glDebugMessageCallbackARB.userParam size not checked against 'callback'
glDebugMessageCallbackARB=wrapper.wrapper(glDebugMessageCallbackARB).setInputArraySize(
    'userParam', None
)
glGetDebugMessageLogARB=wrapper.wrapper(glGetDebugMessageLogARB).setOutput(
    'ids',size=lambda x:(x,),pnameArg='count',orPassIn=True
).setOutput(
    'lengths',size=lambda x:(x,),pnameArg='count',orPassIn=True
).setOutput(
    'messageLog',size=lambda x:(x,),pnameArg='bufSize',orPassIn=True
).setOutput(
    'severities',size=lambda x:(x,),pnameArg='count',orPassIn=True
).setOutput(
    'sources',size=lambda x:(x,),pnameArg='count',orPassIn=True
).setOutput(
    'types',size=lambda x:(x,),pnameArg='count',orPassIn=True
)
### END AUTOGENERATED SECTION