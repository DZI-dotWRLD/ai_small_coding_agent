import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write or overwrite files",
        "parameters": {
            "type": "object",
            "properties": {
                "content":{
                    "type":"string",
                    "description": "String of content which needde to be written inside the file",
                },
                "file_path": {
                    "type": "string",
                    "description": "File path to follow to get to the file",
                },
            },
        },
    },
}


def write_file(working_directory: str, file_path: str, content: str) -> str:
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
        is_dir = os.path.isdir(full_file_path)

        if not common_shared_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if is_dir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        #if needed creating missing folders
        dir_path = os.path.dirname(full_file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        with open(full_file_path,"w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as err:
        print(f"Error: {err}")
