# shader_utils.py
"""
shader_utils.py

This module provides utility functions for compiling and linking shaders in OpenGL.

Functions:
    compile_shader(source, shader_type):
        Compiles a shader of the specified type (vertex or fragment).

    create_shader_program(vertex_source, fragment_source):
        Creates and links a shader program using vertex and fragment shaders.

    load_shader_source(file_path):
        Loads shader source code from a file.
"""

from OpenGL.GL import *

def compile_shader(source, shader_type):
    """
    Compiles a shader of the specified type.

    Parameters:
        source (str): The GLSL source code for the shader.
        shader_type (GLenum): The type of shader (e.g., GL_VERTEX_SHADER, GL_FRAGMENT_SHADER).

    Returns:
        GLuint: The compiled shader ID.

    Raises:
        RuntimeError: If the shader compilation fails.
    """
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)

    # Check for compilation errors
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        error_message = glGetShaderInfoLog(shader).decode()
        shader_type_str = "Vertex" if shader_type == GL_VERTEX_SHADER else "Fragment"
        raise RuntimeError(f"{shader_type_str} shader compilation failed:\n{error_message}")

    return shader

def create_shader_program(vertex_source, fragment_source):
    """
    Creates and links a shader program using vertex and fragment shaders.

    Parameters:
        vertex_source (str): The GLSL source code for the vertex shader.
        fragment_source (str): The GLSL source code for the fragment shader.

    Returns:
        GLuint: The linked shader program ID.

    Raises:
        RuntimeError: If the program linking fails.
    """
    # Compile shaders
    vertex_shader = compile_shader(vertex_source, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(fragment_source, GL_FRAGMENT_SHADER)

    # Create and link the shader program
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)

    # Check for linking errors
    if not glGetProgramiv(program, GL_LINK_STATUS):
        error_message = glGetProgramInfoLog(program).decode()
        raise RuntimeError(f"Shader program linking failed:\n{error_message}")

    # Cleanup: detach and delete shaders
    glDetachShader(program, vertex_shader)
    glDetachShader(program, fragment_shader)
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    return program

def load_shader_source(file_path):
    """
    Loads shader source code from a file.

    Parameters:
        file_path (str): The path to the GLSL shader file.

    Returns:
        str: The shader source code as a string.
    """
    with open(file_path, 'r') as shader_file:
        return shader_file.read()
