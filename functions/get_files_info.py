import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    output = ""
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        else:
            output += f'Success: "{directory}" is within the working directory\n'
            for item in os.listdir(target_dir):
                item_path = os.path.join(target_dir, item)
                output += f'- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}\n'
            return output
    except Exception as e:
        return f"Error: {e}"