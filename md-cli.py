from markitdown import MarkItDown
from pathlib import Path
import os
import re
import typer


app = typer.Typer()


@app.command()
def convert(
    input_path: Path = typer.Argument(..., exists=True, file_okay=True, dir_okay=False),
    output_path: Path = typer.Argument(..., exists=False, file_okay=True, dir_okay=False)
):
    '''
    input_path: 
        Type: Path
        Required: True
        Path to file that will be converted to a .md

    output_path: 
        Type: Path
        Required: True
        Path to what is/will be the .md
    '''

    # Check if the output path ends with .md -> if not: append '.md'.
    if not re.match(r"^.+\.md$", str(output_path)):
        output_path = Path(f"{str(output_path)}.md")

    while os.path.exists(output_path):  # Overwrite an existing file?
        overwrite = input("\nThe supplied output directory already exists. Would you like to overwrite the existing file? (y/n): ")
        match overwrite.lower():
             case "y":
                break
             case "n":
                typer.echo("\nExiting... \nThe file will not be overwritten.\n")
                raise SystemExit()
             case default:
                print("\nNeither y/n was selected.\n")

    # Create a MarkItDown object and convert to markdown
    md = MarkItDown()
    result = md.convert(input_path)

    # Write the markdown to the output path
    with open(f"{output_path}", "w") as f:
        f.write(result.text_content)
 
    # Check that the output path exists
    if os.path.exists(output_path):  
        typer.echo(f"\n{input_path} was successfully converted to markdown. \nExiting...\n")
    else: 
        typer.echo(f"\n{output_path} was not converted to Markdown. \nExiting...\n")


if __name__ == "__main__":
	app()