import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    
    try:
        # get the absolute path of the working directory and the target directory
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # Either true or false, depending on whether the target directory is a subdirectory of the working directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    except Exception as e:
        return f'Error: {str(e)}'

    if not os.path.isdir(directory):
        return  f'Error: "{directory}" is not a directory'

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if valid_target_dir:
        return f'Success: "{directory}" is within the working directory'



    