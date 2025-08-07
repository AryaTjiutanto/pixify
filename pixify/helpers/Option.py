import typer

def parse_size(size_str:str = None):
    if size_str:
        try:
            width, height = map(int ,size_str.lower().split('x'))
            return (width, height)
        except (ValueError, AttributeError):
            raise typer.BadParameter("Size must be in the format WIDTHxHEIGHT, for example: 64x64") 
    return None