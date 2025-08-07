import os

def get_output_path(input_path:str, output_format:str, output_name:str=None, output_folder:str=None):
    if output_name :
        base = os.path.splitext(output_name)[0]
    elif output_folder:
        base = os.path.splitext(os.path.basename(input_path))[0]
    else:
        base = os.path.splitext(input_path)[0]

    if output_folder:
        return f"{output_folder}/{ base }.{ output_format.lower() }"
    else:
        return f"{ base }.{ output_format.lower() }"