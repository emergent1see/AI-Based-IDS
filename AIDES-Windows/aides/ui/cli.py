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
