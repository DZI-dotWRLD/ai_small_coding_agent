import os
from config import MAX_CHARS



def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        # Example abs_path = /home/dzi/workspace/bootdotdev/ai_coding_agent/ai_baby_agent/functions/calculator
        # if working dic calculator
        absolute_path = os.path.abspath(working_directory)
        # builds full absolute path to passed file path
        full_file_path = os.path.normpath(os.path.join(absolute_path, file_path))
        #returns true if the path match
        common_shared_path= os.path.commonpath([absolute_path, full_file_path]) == absolute_path
        #checks if the full path leading to file
        is_file = os.path.isfile(full_file_path)



        if not common_shared_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'



        with open(full_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
    except Exception as err:
        print(f"Error: {err}")




print(get_file_content("calculator", "lorem.txt"))
