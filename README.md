# Figlet Text Generator

A Python program that converts plain text into stylish ASCII art using the pyfiglet library. The program supports both random font selection and specific font selection via command-line arguments.

## Features

- 🎨 **100+ Fonts**: Access to all available pyfiglet fonts
- 🎲 **Random Mode**: Automatically select a random font for your text
- 🎯 **Specific Font Mode**: Choose exactly which font to use
- ⚡ **Command-Line Interface**: Easy to use with command-line arguments
- 🛡️ **Error Handling**: Comprehensive validation and helpful error messages

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Dependencies
Install the required package:
```bash
pip install pyfiglet
```

## Usage

The program expects **zero** or **two** command-line arguments:

### Random Font Mode
```bash
python figlet.py
```
The program will randomly select a font and prompt you for text.

### Specific Font Mode
```bash
python figlet.py -f FONT_NAME
python figlet.py --font FONT_NAME
```
Replace `FONT_NAME` with your desired font.

## Examples

### Random Font
```bash
$ python figlet.py
What do you want to display: Hello World
  _   _      _ _        __        __         _     _ 
 | | | | ___| | | ___   \ \      / /__  _ __| | __| |
 | |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` |
 |  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |
 |_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_|
```

### Specific Font
```bash
$ python figlet.py -f slant
What do you want to display: CS50
    ________ ______   ____ 
   / ____/ //_/ __ ) / __ \
  / /   / ,< / __  |/ / / /
 / /___/ /| / /_/ / /_/ / 
 \____/_/ |_/_____/\____/
```

### Popular Font Names
- `slant` - Italic-style text
- `block` - Bold block letters
- `script` - Cursive handwriting
- `digital` - LCD display style
- `bubble` - Rounded bubble letters
- `standard` - Classic ASCII art

## Error Handling

The program validates all inputs and provides clear error messages:

- **Invalid argument count**: `Invalid usage`
- **Wrong flag**: `Invalid Usage` (when not using `-f` or `--font`)
- **Invalid font name**: `Invalid usage`

## Project Structure
```
figlet.py          # Main program file
```

## How It Works

1. **Argument Parsing**: Checks command-line arguments for valid patterns
2. **Font Selection**: Either randomly picks a font or uses the specified one
3. **Text Input**: Prompts user for text to convert
4. **Rendering**: Uses pyfiglet to generate ASCII art
5. **Output**: Displays the formatted text

