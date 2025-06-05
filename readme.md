# Connect 4 Bot - Contest Edition

## Overview
This is a Connect Four game that features the AI Agent in a human vs. AI gameplay mode, with options for both graphical and command-line interfaces.

## Installation
No installation required - simply use the provided executable file.

## How to Run

### Option 1: Double-Click Execution
1. Navigate to `dist`
2. Double-click `contest.exe` to run with default settings (human starts first, graphical interface)

### Option 2: Command Line Execution
1. Open PowerShell or Command Prompt
2. Navigate to the distribution folder:
   ```powershell
   cd "dist"
   ```
3. Run the executable with optional arguments:
   ```powershell
   .\contest.exe [arg1] [arg2]
   ```

## Command Line Arguments

| Argument | Values | Description | Default |
|----------|--------|-------------|---------|
| arg1 | `a` or `h` | `a` - AI starts first<br>`h` - Human starts first | `h` |
| arg2 | `g` or `c` | `g` - Graphical interface<br>`c` - Command-line interface | `g` |

### Examples:
- AI starts first with graphical interface:
  ```powershell
  .\contest.exe a g
  ```
- Human starts first with command-line interface:
  ```powershell
  .\contest.exe h c
  ```
- Default settings (same as double-click):
-- Human starts first with graphical interface
  ```powershell
  .\contest.exe
  ```

## Game Controls
### Graphical Interface:
- Click on a column to drop your piece
- Close window or use in-game quit option to exit

### Command-line Interface:
- Enter column number (0-6) to drop your piece
- Enter `-1` to quit the game

## File Structure
| File | Description |
|------|-------------|
| `contest.exe` | Main executable file |
| `contest.py` | Contains the AI model implementation |
| `encode.py` | Contains the board state encoder |

## Troubleshooting
- For "file not found" errors in PowerShell:
  - Always use `.\` prefix when running executables
  - Example: `.\contest.exe` instead of just `contest.exe`

## Development Notes
To modify the AI behavior, edit `contest.py` which contains the core AI logic. The encoder in `encode.py` encodes board state representations from the Connect 4 dataset (`\connect+4\connect-4.data.Z`, pulled from https://archive.ics.uci.edu/dataset/26/connect+4) for the AI.