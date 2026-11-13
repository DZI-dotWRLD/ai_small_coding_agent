import os
import subprocess


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run Python files with optional arguments",
        "parameters": {
            "type": "object",
            "properties": {
                "args":{
                    "type":"list[str] | None = None",
                    "description": "List of string with additional arguments",
                },
                "file_path": {
                    "type": "string",
                    "description": "File path to follow to get to the file which would be executed",
                },
            },
        },
    },
}

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:

    try:

        absolute_path = os.path.abspath(working_directory)
        # builds full absolute path to passed file path
        full_file_path = os.path.normpath(os.path.join(absolute_path, file_path))
        #returns true if the path match
        common_shared_path= os.path.commonpath([absolute_path, full_file_path]) == absolute_path
        is_file = os.path.isfile(full_file_path)


        if not common_shared_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not is_file:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not full_file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", full_file_path]

        if args is not None:
            command.extend(args)

        sub_process = subprocess.run(command, cwd=working_directory, capture_output=True, text=True, timeout=30 )
        output = []
        if sub_process.returncode != 0:
            output.append(f"Process exited with code {sub_process.returncode}")
        if len(sub_process.stdout) == 0 and len(sub_process.stderr) == 0:
            output.append("No output produced")

        if len(sub_process.stdout) > 0:
            output.append(f"STDOUT: {sub_process.stdout}")

        if len(sub_process.stderr) > 0:
            output.append(f"STDERR: {sub_process.stderr}")

        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
