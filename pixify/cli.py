import typer
from typing import Optional
from pixify.services.converter import convert_image, convert_all_image_in_folder
import os

app = typer.Typer()

@app.command()
def convert(
        input_path: Optional[str] = typer.Argument(
            None, 
            help="Path to a single image file. Ignored if using 'all' mode."
        ),
        mode: str = typer.Option(
            "path",
            "--mode", "-m", 
            help="Conversion mode: 'path' to convert a single file, or 'all' to convert all images in a folder."
        ),
        output_format: str = typer.Option(
            ..., 
            "--to", "-t", 
            help="Target image format (e.g. png, jpg, webp)."
        ),
        input_folder: Optional[str] = typer.Option(
            None,
            "--folder", "-f",
            help="Path to the folder containing images to convert (used only with 'all' mode)."
        ),
        output_folder: Optional[str] = typer.Option(
            None,
            "--output-folder", "-of",
            help="Destination folder for converted files. Will be created if it doesn't exist."
        ),
        output_name: Optional[str] = typer.Option(
            None,
            "--output-name", "-on",
            help="Custom name for the output file (used only in single-file mode)."
        ),
        format_filter: Optional[str] = typer.Option(
            None, 
            "--ext", "-e", 
            help="Filter by file extension when using 'all' mode (e.g. jpg)."
        ),
        size: Optional[str] = typer.Option(
            None,
            "--size", '-s',
            help="Output image size in WIDTHxHEIGHT format (example: 64x64).",
        )
    ):
    # handle jpg 
    output_format = output_format.lower()
    if output_format == 'jpg':
        output_format = 'jpeg'

    # Ensure output folder exists
    if output_folder:
        os.makedirs(output_folder, exist_ok=True)

    # hadnle mode
    if(mode == "path"):
        if not input_path:
            typer.echo("❌ Error: You must provide --input-path in 'path' mode.")
            raise typer.Exit(code=1)
         
        convert_image(input_path, output_format, output_name, size, output_folder)
    elif(mode == "all"):
        convert_all_image_in_folder(input_folder, output_format, format_filter, size, output_folder)
    else:
        typer.echo(f"❌ Error: Invalid mode '{mode}'. Use 'path' or 'all'.")
        raise typer.Exit(code=1)

def main():
    app()

if __name__ == '__main__':
    app()