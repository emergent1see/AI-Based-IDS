#!/usr/bin/env python3
"""
bootstrap.py
Creates the AIDES-Windows project skeleton with starter files.
Run: python bootstrap.py
"""

import os
import textwrap

ROOT = "AIDES-Windows"

FILES = {
    # top-level
    f"{ROOT}/README.md": "# AIDES-Windows\n\nSecurity telemetry + ML on Windows. Scaffold created by bootstrap.py\n",
    f"{ROOT}/requirements.txt": textwrap.dedent("""\
        psutil
        pywin32
        sqlite3-binary; platform_system == "Windows"
        pyyaml
        pytest
        rich
        scikit-learn
    """),
    f"{ROOT}/pyproject.toml": textwrap.dedent("""\
        [build-system]
        requires = ["setuptools", "wheel"]
        build-backend = "setuptools.build_meta"
    """),
    f"{ROOT}/setup.py": textwrap.dedent("""\
        from setuptools import setup, find_packages
        setup(
            name='AIDES-Windows',
            version='0.1.0',
            packages=find_packages(),
            include_package_data=True,
            install_requires=[
                'psutil', 'pyyaml', 'rich'
            ],
            entry_points={
                'console_scripts': [
                    'aides-windows = aides.main:cli_entry'
                ]
            }
        )
    """),
    f"{ROOT}/LICENSE": "MIT License\n",

    # config files
    f"{ROOT}/config/config.yaml": textwrap.dedent("""\
        app:
          name: AIDES-Windows
          log_level: INFO
        collectors:
          enable_etw: true
          enable_wmi: true
        storage:
          sqlite_path: data/aides.db
        ml:
          model_dir: data/models
    """),
    f"{ROOT}/config/etw_providers.json": "[]\n",
    f"{ROOT}/config/model_config.yaml": "model: default\n",
    f"{ROOT}/config/alert_rules.yaml": textwrap.dedent("""\
        - id: suspicious-process
          description: 'Process launching from temp directory'
          severity: high
    """),

    # top-level dirs
    f"{ROOT}/scripts/install.bat": textwrap.dedent(r"""\
        @echo off
        REM Example install script - register service using nssm or pywin32
        echo Installing AIDES-Windows service...
        REM You can use nssm to wrap python script as service:
        REM nssm install AIDES-Windows "C:\Python39\python.exe" "%~dp0\..\aides\main.py"
        echo Done.
    """),
    f"{ROOT}/scripts/uninstall.bat": "@echo off\nREM Uninstall script placeholder\n",
    f"{ROOT}/scripts/service_install.py": textwrap.dedent('''\
        # Example: use pywin32 to create a Windows service (requires implementation)
        # This file is a template; implementing a robust service wrapper is non-trivial.
        # See: https://github.com/mhammond/pywin32
        def install_service():
            print("Service installation example - implement using pywin32 or nssm.")
    '''),
    f"{ROOT}/scripts/update_models.py": textwrap.dedent('''\
        # sample script to update models
        from pathlib import Path
        def main():
            print("update models - implement model download or retraining here")
        if __name__ == "__main__":
            main()
    '''),
    f"{ROOT}/scripts/generate_training_data.py": textwrap.dedent('''\
        # script to create synthetic training data
        import json
        def main():
            print("Generate synthetic training data")
        if __name__ == "__main__":
            main()
    '''),

    # data dirs placeholder
    f"{ROOT}/data/.gitkeep": "",
    f"{ROOT}/data/models/.gitkeep": "",
    f"{ROOT}/data/training/.gitkeep": "",
    f"{ROOT}/data/logs/.gitkeep": "",
    f"{ROOT}/data/events/.gitkeep": "",

    # docs
    f"{ROOT}/docs/installation.md": "# Installation\n",
    f"{ROOT}/docs/configuration.md": "# Configuration\n",
    f"{ROOT}/docs/api_reference.md": "# API Reference\n",
    f"{ROOT}/docs/development.md": "# Development\n",

    # tests
    f"{ROOT}/tests/__init__.py": "",
    f"{ROOT}/tests/test_collectors.py": textwrap.dedent('''\
        def test_collectors_import():
            import aides.collectors
            assert True
    '''),
    f"{ROOT}/tests/test_features.py": "def test_features():\n    assert True\n",
    f"{ROOT}/tests/test_ml.py": "def test_ml():\n    assert True\n",
    f"{ROOT}/tests/test_integration.py": "def test_integration():\n    assert True\n",

    # package skeleton main files
    f"{ROOT}/aides/__init__.py": "__version__ = '0.1.0'\n",
    f"{ROOT}/aides/version.py": "__version__ = '0.1.0'\n",
    f"{ROOT}/aides/config.py": textwrap.dedent('''\
        import yaml
        from pathlib import Path
        config_path = Path(__file__).parent.parent / "config" / "config.yaml"
        def load_config(path=None):
            p = Path(path) if path else config_path
            with open(p, "r") as fh:
                return yaml.safe_load(fh)
    '''),
    f"{ROOT}/aides/logger.py": textwrap.dedent('''\
        import logging
        def get_logger(name=__name__, level=logging.INFO):
            logger = logging.getLogger(name)
            if not logger.handlers:
                h = logging.StreamHandler()
                fmt = logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
                h.setFormatter(fmt)
                logger.addHandler(h)
            logger.setLevel(level)
            return logger
    '''),

    # main
    f"{ROOT}/aides/main.py": textwrap.dedent('''\
        import argparse
        from .ui.cli import cli
        def cli_entry():
            cli()
        if __name__ == "__main__":
            cli()
    '''),

    # ui
    f"{ROOT}/aides/ui/__init__.py": "",
    f"{ROOT}/aides/ui/cli.py": textwrap.dedent('''\
        import argparse
        from ..logger import get_logger
        from ..collectors.process_monitor import ProcessMonitor
        def cli():
            parser = argparse.ArgumentParser(prog="aides-windows")
            parser.add_argument("--run-once", action="store_true")
            args = parser.parse_args()
            logger = get_logger("aides")
            logger.info("Starting AIDES-Windows")
            if args.run_once:
                pm = ProcessMonitor()
                pm.sample()
                logger.info("Run-once complete")
            else:
                logger.info("Interactive mode - implement scheduler")
    '''),
    f"{ROOT}/aides/ui/console.py": textwrap.dedent('''\
        from rich.console import Console
        console = Console()
        def print_status(msg):
            console.print(msg)
    '''),

    # collectors
    f"{ROOT}/aides/collectors/__init__.py": "",
    f"{ROOT}/aides/collectors/base_collector.py": textwrap.dedent('''\
        from abc import ABC, abstractmethod
        class BaseCollector(ABC):
            def __init__(self, config=None):
                self.config = config
            @abstractmethod
            def start(self): ...
            @abstractmethod
            def stop(self): ...
            @abstractmethod
            def sample(self): ...
    '''),
    f"{ROOT}/aides/collectors/process_monitor.py": textwrap.dedent('''\
        import psutil
        from .base_collector import BaseCollector
        class ProcessMonitor(BaseCollector):
            def __init__(self, config=None):
                super().__init__(config)
            def start(self): pass
            def stop(self): pass
            def sample(self):
                procs = []
                for p in psutil.process_iter(['pid','name','exe','create_time']):
                    procs.append(p.info)
                return procs
    '''),
    f"{ROOT}/aides/collectors/network_monitor.py": textwrap.dedent('''\
        from .base_collector import BaseCollector
        class NetworkMonitor(BaseCollector):
            def sample(self):
                # placeholder: use psutil.net_io_counters() or pyshark for packet capture
                return {}
    '''),
    f"{ROOT}/aides/collectors/file_monitor.py": textwrap.dedent('''\
        from .base_collector import BaseCollector
        class FileMonitor(BaseCollector):
            def sample(self):
                # placeholder: integrate watchdog for file system events
                return {}
    '''),
    f"{ROOT}/aides/collectors/wmi_collector.py": textwrap.dedent('''\
        from .base_collector import BaseCollector
        class WMICollector(BaseCollector):
            def sample(self):
                # placeholder: use wmi or pywin32
                return {}
    '''),
    f"{ROOT}/aides/collectors/etw_collector.py": textwrap.dedent('''\
        from .base_collector import BaseCollector
        class ETWCollector(BaseCollector):
            def sample(self):
                # ETW on windows: integrate with ETW provider libraries
                return {}
    '''),

    # features
    f"{ROOT}/aides/features/__init__.py": "",
    f"{ROOT}/aides/features/base_extractor.py": textwrap.dedent('''\
        from abc import ABC, abstractmethod
        class BaseExtractor(ABC):
            @abstractmethod
            def extract(self, raw):
                pass
    '''),
    f"{ROOT}/aides/features/process_features.py": textwrap.dedent('''\
        from .base_extractor import BaseExtractor
        class ProcessFeatures(BaseExtractor):
            def extract(self, proc_list):
                feats = []
                for p in proc_list:
                    feats.append({
                        "pid": p.get("pid"),
                        "name": p.get("name"),
                    })
                return feats
    '''),
    f"{ROOT}/aides/features/network_features.py": "from .base_extractor import BaseExtractor\n",
    f"{ROOT}/aides/features/file_features.py": "from .base_extractor import BaseExtractor\n",
    f"{ROOT}/aides/features/system_features.py": "from .base_extractor import BaseExtractor\n",

    # ml
    f"{ROOT}/aides/ml/__init__.py": "",
    f"{ROOT}/aides/ml/model_manager.py": textwrap.dedent('''\
        import joblib
        from pathlib import Path
        class ModelManager:
            def __init__(self, model_dir):
                self.model_dir = Path(model_dir)
                self.model_dir.mkdir(parents=True, exist_ok=True)
            def load(self, name):
                p = self.model_dir / f"{name}.pkl"
                if p.exists():
                    return joblib.load(p)
                return None
            def save(self, name, model):
                joblib.dump(model, self.model_dir / f"{name}.pkl")
    '''),
    f"{ROOT}/aides/ml/anomaly_detector.py": textwrap.dedent('''\
        class AnomalyDetector:
            def __init__(self):
                pass
            def predict(self, features):
                # return False for normal, True for anomaly (stub)
                return [False for _ in features]
    '''),
    f"{ROOT}/aides/ml/trainer.py": "class Trainer: pass\n",
    f"{ROOT}/aides/ml/preprocessor.py": "def preprocess(features):\n    return features\n",
    f"{ROOT}/aides/ml/ensemble.py": "class Ensemble: pass\n",

    # storage
    f"{ROOT}/aides/storage/__init__.py": "",
    f"{ROOT}/aides/storage/database.py": textwrap.dedent('''\
        import sqlite3
        from pathlib import Path
        class Database:
            def __init__(self, db_path):
                p = Path(db_path)
                p.parent.mkdir(parents=True, exist_ok=True)
                self.conn = sqlite3.connect(str(p))
                self._ensure_tables()
            def _ensure_tables(self):
                c = self.conn.cursor()
                c.execute(\"\"\"CREATE TABLE IF NOT EXISTS events(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ts DATETIME DEFAULT CURRENT_TIMESTAMP,
                    type TEXT,
                    payload TEXT
                )\"\"\")
                self.conn.commit()
            def insert_event(self, type_, payload):
                c = self.conn.cursor()
                c.execute("INSERT INTO events(type,payload) VALUES(?,?)", (type_, payload))
                self.conn.commit()
    '''),
    f"{ROOT}/aides/storage/event_store.py": "from .database import Database\n",
    f"{ROOT}/aides/storage/model_store.py": "from ..ml.model_manager import ModelManager\n",
    f"{ROOT}/aides/storage/cache.py": "class Cache: pass\n",

    # alerting
    f"{ROOT}/aides/alerting/__init__.py": "",
    f"{ROOT}/aides/alerting/alert_engine.py": textwrap.dedent('''\
        class AlertEngine:
            def __init__(self):
                pass
            def raise_alert(self, rule_id, context):
                print("ALERT", rule_id, context)
    '''),
    f"{ROOT}/aides/alerting/notifier.py": textwrap.dedent('''\
        class Notifier:
            def send(self, channel, payload):
                print("Notify", channel, payload)
    '''),
    f"{ROOT}/aides/alerting/response_engine.py": "class ResponseEngine: pass\n",
    f"{ROOT}/aides/alerting/correlation.py": "class Correlation: pass\n",

    # utils
    f"{ROOT}/aides/utils/__init__.py": "",
    f"{ROOT}/aides/utils/helpers.py": "def ensure_dir(p):\n    import os\n    os.makedirs(p, exist_ok=True)\n",
    f"{ROOT}/aides/utils/security.py": "def secure_defaults():\n    return {}\n",
    f"{ROOT}/aides/utils/windows_helpers.py": textwrap.dedent('''\
        # Windows-specific helper functions
        import platform
        def is_windows():
            return platform.system() == "Windows"
    '''),
    f"{ROOT}/aides/utils/performance.py": "def measure(): pass\n",

    # integration
    f"{ROOT}/aides/integration/__init__.py": "",
    f"{ROOT}/aides/integration/active_directory.py": "class ADIntegration: pass\n",
    f"{ROOT}/aides/integration/antivirus.py": "class AVIntegration: pass\n",
    f"{ROOT}/aides/integration/siem.py": "class SIEMIntegration: pass\n",

    # tests for package import
    f"{ROOT}/tests/test_imports.py": textwrap.dedent('''\
        def test_import_package():
            import aides
            assert hasattr(aides, "__version__")
    '''),

    # GitHub Actions CI
    f"{ROOT}/.github/workflows/python-app.yml": textwrap.dedent('''\
        name: Python package
        on: [push, pull_request]
        jobs:
          build:
            runs-on: windows-latest
            steps:
            - uses: actions/checkout@v4
            - name: Set up Python
              uses: actions/setup-python@v4
              with:
                python-version: '3.10'
            - name: Install dependencies
              run: |
                python -m pip install --upgrade pip
                pip install -r requirements.txt
            - name: Run tests
              run: pytest -q
    '''),
}

def ensure_dirs():
    dirs = [
        f"{ROOT}/aides/collectors",
        f"{ROOT}/aides/features",
        f"{ROOT}/aides/ml",
        f"{ROOT}/aides/storage",
        f"{ROOT}/aides/alerting",
        f"{ROOT}/aides/ui",
        f"{ROOT}/aides/utils",
        f"{ROOT}/aides/integration",
        f"{ROOT}/config",
        f"{ROOT}/data",
        f"{ROOT}/data/models",
        f"{ROOT}/docs",
        f"{ROOT}/scripts",
        f"{ROOT}/tests",
        f"{ROOT}/.github/workflows",
    ]
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def write_files():
    for path, content in FILES.items():
        d = os.path.dirname(path)
        if d and not os.path.exists(d):
            os.makedirs(d, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
    print(f"Scaffold created at ./{ROOT}")

if __name__ == "__main__":
    ensure_dirs()
    write_files()
