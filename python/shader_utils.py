"""
shader_utils.py

This module provides utility functions for compiling and linking shaders in OpenGL.

Functions:
-----------
compile_shader(source, shader_type):
    Compiles a shader of the specified type (vertex, fragment, or geometry).

create_shader_program(vertex_source, fragment_source, geometry_source=None):
    Creates and links a shader program using vertex, fragment, and optionally, a geometry shader.

load_shader_source(file_path):
    Loads shader source code from a file.
"""

import logging
from OpenGL.GL import *

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def compile_shader(source, shader_type):
    """
    Compiles a shader of the specified type.

    Parameters:
        source (str): The GLSL source code for the shader.
        shader_type (GLenum): The type of shader (GL_VERTEX_SHADER, GL_FRAGMENT_SHADER, GL_GEOMETRY_SHADER).

    Returns:
        GLuint: The compiled shader ID.

    Raises:
        RuntimeError: If shader compilation fails.
    """
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)

    # Check for compilation errors
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        error_message = glGetShaderInfoLog(shader).decode()
        shader_type_str = {
            GL_VERTEX_SHADER: "Vertex",
            GL_FRAGMENT_SHADER: "Fragment",
            GL_GEOMETRY_SHADER: "Geometry"
        }.get(shader_type, "Unknown")
        
        logging.error(f"{shader_type_str} shader compilation failed:\n{error_message}")
        raise RuntimeError(f"{shader_type_str} shader compilation failed:\n{error_message}")

    logging.info(f"{shader_type_str} shader compiled successfully.")
    return shader

def create_shader_program(vertex_source, fragment_source, geometry_source=None):
    """
    Creates and links a shader program using vertex, fragment, and optionally, a geometry shader.

    Parameters:
        vertex_source (str): The GLSL source code for the vertex shader.
        fragment_source (str): The GLSL source code for the fragment shader.
        geometry_source (str, optional): The GLSL source code for the geometry shader.

    Returns:
        GLuint: The linked shader program ID.

    Raises:
        RuntimeError: If program linking fails.
    """
    # Compile shaders
    vertex_shader = compile_shader(vertex_source, GL_VERTEX_SHADER)
    fragment_shader = compile_shader(fragment_source, GL_FRAGMENT_SHADER)

    # Create and link the shader program
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)

    geometry_shader = None
    if geometry_source:
        geometry_shader = compile_shader(geometry_source, GL_GEOMETRY_SHADER)
        glAttachShader(program, geometry_shader)

    glLinkProgram(program)

    # Check for linking errors
    if not glGetProgramiv(program, GL_LINK_STATUS):
        error_message = glGetProgramInfoLog(program).decode()
        logging.error(f"Shader program linking failed:\n{error_message}")
        raise RuntimeError(f"Shader program linking failed:\n{error_message}")

    logging.info("Shader program linked successfully.")

    # Cleanup: Detach and delete shaders
    glDetachShader(program, vertex_shader)
    glDetachShader(program, fragment_shader)
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    if geometry_shader:
        glDetachShader(program, geometry_shader)
        glDeleteShader(geometry_shader)

    return program

def load_shader_source(file_path):
    """
    Loads shader source code from a file.

    Parameters:
        file_path (str): The path to the GLSL shader file.

    Returns:
        str: The shader source code as a string.

    Raises:
        FileNotFoundError: If the file cannot be found.
        IOError: If there's an issue reading the file.
    """
    try:
        with open(file_path, 'r') as shader_file:
            logging.info(f"Loaded shader source from {file_path}")
            return shader_file.read()
    except FileNotFoundError:
        logging.error(f"Shader file not found: {file_path}")
        raise
    except IOError as e:
        logging.error(f"Error reading shader file {file_path}: {e}")
        raise
