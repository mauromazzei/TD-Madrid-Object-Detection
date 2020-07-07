'''OpenGL extension ANDROID.native_fence_sync

This module customises the behaviour of the 
OpenGL.raw.EGL.ANDROID.native_fence_sync to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ANDROID/native_fence_sync.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.EGL import _types, _glgets
from OpenGL.raw.EGL.ANDROID.native_fence_sync import *
from OpenGL.raw.EGL.ANDROID.native_fence_sync import _EXTENSION_NAME

def glInitNativeFenceSyncANDROID():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION