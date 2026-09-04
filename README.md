# mouse-automation-45

A high-performance, cross-platform automation utility designed for precise mouse clicking and macro execution. This tool leverages Python to provide a lightweight solution for repetitive desktop tasks.

## Features

*   **Adaptive Click Intervals:** Support for custom millisecond-based delay configurations to mimic human behavior or maximize input speed.
*   **Dynamic Targeting:** Built-in screen coordinate detection, allowing for pixel-perfect automation on specific UI elements.
*   **Safety Overrides:** Integrated "Fail-Safe" mode that instantly halts all scripts when the mouse is moved to a corner of the screen.
*   **Low-Overhead Execution:** Optimized event loop processing to ensure minimal CPU usage during prolonged automation sessions.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/mouse-automation-45.git
cd mouse-automation-45
pip install -r requirements.txt
```

## Usage

You can initialize a basic autoclicker sequence by running the following command in your terminal:

```python
from mouse_automation import Clicker

# Configure a clicker with a 100ms interval
bot = Clicker(interval=0.1)

# Start clicking at the current cursor position
bot.start()
```

For advanced usage, including coordinate mapping and specific key-binding triggers, refer to the [documentation folder](/docs).

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.