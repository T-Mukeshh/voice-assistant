# Voice Assistant

A sophisticated, voice-controlled desktop assistant that brings hands-free productivity to your workflow. Execute system commands, manage applications, and control your PC using natural voice interactions—no keyboard or mouse required.

## Features

- **Voice Command Recognition** - Understand and execute natural language voice commands
- **Application Launcher** - Launch applications and open files with voice control
- **System Management** - Adjust settings, manage files, and perform system operations
- **Text-to-Speech** - Hear responses and confirmations through audio feedback
- **Web-Based Interface** - Clean, intuitive UI built with modern web technologies
- **Extensible Architecture** - Easy to add new commands and features

## Requirements

- **Python 3.8+**
- **Operating System**: Windows (currently optimized for Windows systems)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd voice-assistant
```

### 2. Set Up Python Environment

Create a virtual environment to isolate dependencies:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Core Dependencies:**
- `eel` - Python-JavaScript bridge for desktop app
- `speechrecognition` - Voice input recognition
- `pyttsx3` - Text-to-speech output
- `selenium` - Web automation capabilities

## Usage

### Starting the Assistant

```bash
python main.py
```

The application will launch with a web-based interface. Speak your commands clearly for best recognition.

### Example Commands

- "Open notepad"
- "What time is it?"
- "Close this window"
- "Launch Chrome"

## Project Structure

```
voice-assistant/
├── main.py                 # Application entry point
├── engine/                 # Core voice processing engine
│   ├── command.py         # Command parsing and execution
│   ├── config.py          # Configuration settings
│   ├── features.py        # Feature modules
│   ├── search_engine.py   # Search functionality
│   └── test.py            # Engine tests
├── models/                # Machine learning models (if applicable)
├── www/                   # Web interface
│   ├── index.htm          # Main UI
│   ├── main.js            # Client-side logic
│   ├── controller.js      # UI controller
│   ├── style.css          # Styling
│   └── assets/            # Static resources
├── data/                  # Data files and configurations
└── README.md              # This file
```

## Getting Started Guide

1. **Ensure Microphone**: Connect a working microphone to your system
2. **Configure Settings**: Edit `engine/config.py` to customize commands
3. **Run the App**: Execute `python main.py`
4. **Grant Permissions**: Allow microphone access when prompted
5. **Start Speaking**: Use voice commands to control your system

## Troubleshooting

- **Microphone not detected**: Check system audio settings and permissions
- **Poor recognition**: Speak clearly and reduce background noise
- **Commands not executing**: Verify command syntax in `engine/command.py`

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance functionality.

## License

This project is open source and available for educational and personal use.

---

**Questions or Issues?** Open an issue on the repository for support.
