This repository provides a \[relatively] easy way to use MarkItDown from a CLI.

[MarkItDown](https://github.com/microsoft/markitdown) is a Python tool for converting files and office documents to Markdown.

**Note**:
- As of right now, markitdown-cli only works on Linux (I have only tested it on Ubuntu 24.04). I do plan on implementing markitdown-cli on Windows at some point.
- markitdown-cli does not support image files.

## Installation

``` bash
# Insert shebang at line 1
sed -i '1i #!/usr/local/lib/md-cli/.venv/bin/python' md-cli.py 

# Move and make script executable
sudo cp md-cli.py /usr/local/bin/md-cli
sudo chmod +x /usr/local/bin/md-cli

# Create /usr/local/lib/md-cli/ and copy requirements.txt
sudo mkdir /usr/local/lib/md-cli
sudo cp requirements.txt /usr/local/lib/md-cli

# Create & activate .venv and install dependencies
cd /usr/local/lib/md-cli
sudo python3 -m venv .venv
sudo source .venv/bin/activate
pip install -r requirements.txt

# Install ffmpeg
sudo apt update && sudo apt upgrade -y
sudo apt install ffmpeg
```

## Usage
Use:

```
md-cli convert INPUT_FILE OUTPUT_FILE
```
