import logging
from utils.logger import setup_logger
from utils.scheduler import Scheduler
from utils.notifier import Notifier
import importlib
import os
import yaml

# Load config
CONFIG_FILE = "config.yaml"
PLUGINS_DIR = "plugins"

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def load_plugins(plugins_dir, enabled_plugins):
    plugins = []
    for plugin_name in enabled_plugins:
        module_path = f"{plugins_dir}.{plugin_name}"
        try:
            module = importlib.import_module(module_path)
            plugin = getattr(module, "Plugin")()
            plugins.append(plugin)
        except Exception as e:
            logging.error(f"Failed to load plugin {plugin_name}: {e}")
    return plugins

def main():
    config = load_config(CONFIG_FILE)
    setup_logger(config.get("logging", {}))

    notifier = Notifier(config.get("notifications", {}))
    scheduler = Scheduler()

    plugins = load_plugins("plugins", config.get("enabled_plugins", []))

    for plugin in plugins:
        scheduler.add_plugin(plugin, notifier, config)

    print("Automation Agent started. Press Ctrl+C to exit.")
    try:
        scheduler.run()
    except KeyboardInterrupt:
        print("Shutting down agent...")

if __name__ == "__main__":
    main()