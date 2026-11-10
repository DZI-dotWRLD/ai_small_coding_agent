import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, directory))
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path
        ispath = os.path.isdir(target_dir)

        if valid_target_dir and ispath:
            return f'Success: "{directory}" is within the working directory'
        elif not ispath:
            return f'Error: "{directory}" is not a directory'
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as err:
        print(f"Error: {err}")
