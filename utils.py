import time
import logging
import threading
from typing import Callable, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('mouse-automation')

class ClickerController:
    def __init__(self):
        self._running = False
        self._lock = threading.Lock()

    def start(self, task: Callable[[], Any], interval: float):
        with self._lock:
            self._running = True
        
        def runner():
            while self._running:
                task()
                time.sleep(interval)
        
        thread = threading.Thread(target=runner, daemon=True)
        thread.start()

    def stop(self):
        with self._lock:
            self._running = False
        logger.info('clicker process terminated successfully')

def validate_interval(value: float) -> float:
    if value < 0.001:
        logger.warning('interval too low, resetting to 0.001s')
        return 0.001
    return value