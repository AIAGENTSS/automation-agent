# automation-agent
Monitoring a directory for new files and logging their names.
# Automation Agent

A simple Python automation agent that monitors a directory (`watched/`) for new files and logs their arrival.

## Features

- Monitors a folder for new files
- Logs events to `agent.log`
- Easily extensible for more automation tasks

## Usage

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd automation-agent
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the agent:**
   ```bash
   python agent.py
   ```

5. **Add new files to the `watched/` directory.**  
   The agent will log any new files detected.

## Customization

- Modify `agent.py` to add more automation behaviors (e.g., send notifications, process files, etc).

## License

MIT
