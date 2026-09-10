import ctypes
import time
import threading

class PerformanceClicker:
    """A high-performance autoclicker utilizing direct Windows API calls for minimal latency."""
    
    # Windows API constants for mouse events
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004

    def __init__(self, interval_seconds: float = 0.001):
        self.interval = interval_seconds
        self.is_clicking = False
        self._thread = None
        # Cache the user32 reference to minimize lookup overhead in the tight loop
        self._user32 = ctypes.windll.user32

    def start(self) -> None:
        """Starts the high-frequency clicking thread if not already running."""
        if not self.is_clicking:
            self.is_clicking = True
            self._thread = threading.Thread(target=self._click_loop, daemon=True)
            self._thread.start()

    def stop(self) -> None:
        """Stops the clicking loop and blocks until the thread terminates."""
        self.is_clicking = False
        if self._thread:
            self._thread.join(timeout=1.0)

    def _click_loop(self) -> None:
        """Optimized inner loop utilizing high-precision timing and direct DLL calls."""
        interval = self.interval
        user32 = self._user32
        down_flag = self.MOUSEEVENTF_LEFTDOWN
        up_flag = self.MOUSEEVENTF_LEFTUP
        
        next_click = time.perf_counter()
        
        while self.is_clicking:
            now = time.perf_counter()
            if now >= next_click:
                # Direct C function calls to bypass Python wrapper overhead
                user32.mouse_event(down_flag, 0, 0, 0, 0)
                user32.mouse_event(up_flag, 0, 0, 0, 0)
                
                # Calculate next target time to maintain precise frequency
                next_click = now + interval
                
            # Adaptive micro-sleep to prevent 100% CPU utilization
            sleep_time = next_click - time.perf_counter()
            if sleep_time > 0.0005:
                time.sleep(sleep_time)