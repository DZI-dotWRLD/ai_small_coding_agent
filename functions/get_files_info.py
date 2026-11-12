import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        absolute_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_path, directory))
        valid_target_dir = os.path.commonpath([absolute_path, target_dir]) == absolute_path
        isdir = os.path.isdir(target_dir)




        if valid_target_dir and isdir:
            result = []
            for item in os.listdir(target_dir):
                full_path = os.path.join(target_dir, item)
                size = os.path.getsize(full_path)
                is_dir = os.path.isdir(full_path)
                result.append(f" - {item}: file_size={size}, is_dir={is_dir}")
            return "\n".join(result)
        elif not isdir:
            return f'Error: "{directory}" is not a directory'
        else:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    except Exception as err:
        print(f"Error: {err}")
