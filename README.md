# WindowGotchi

A simple desktop virtual pet inspired by Tamagotchi. The prototype is written in Python using Tkinter for the UI.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Project Structure

- `main.py`: Main entry point
- `src/`: Source code modules
- `tests/`: Test files
- `tauri-app/`: Tauri-based Rust + web prototype

## Building the Tauri App

The `tauri-app/` folder contains an experimental Tauri version of WindowGotchi.
To build it you need a recent Node.js and Rust toolchain installed. Then run:

```bash
cd tauri-app
npm install
npm run build        # compile TypeScript
npm run tauri-build  # build the desktop app
```

During development you can launch it with:

```bash
npm run tauri
```

This will start the Tauri dev environment and open the application window.
