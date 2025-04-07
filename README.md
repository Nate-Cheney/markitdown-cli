This repository provides a \[relatively] easy way to use MarkItDown from a CLI.

[MarkItDown](https://github.com/microsoft/markitdown) is a Python tool for converting files and office documents to Markdown.

**Note**:
- As of right now, markitdown-cli only works on Linux (I have only tested it on Ubuntu 24.04). I do plan on implementing markitdown-cli on Windows at some point.
- markitdown-cli does not support image files.

## Installation

``` bash
# Install dependencies
python3 -m pip install 'markitdown[all]' typer

# Create the executable script
echo '#!/usr/bin/env python3' > md-cli
cat md-cli.py >> md-cli
chmod +x md-cli

# Move the script to ~/bin
sudo mv md-cli /usr/local/bin
```

## Usage
Use:

```
md-cli INPUT_FILE OUTPUT_FILE
```
