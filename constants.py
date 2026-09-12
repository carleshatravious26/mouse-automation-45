import sys

# Optimized event timings for low-latency click execution
# Milliseconds define the overhead between internal cycles
MIN_CLICK_INTERVAL_MS = 0.01
MAX_CLICK_INTERVAL_MS = 1000.0

# Hardware acceleration defaults
# Setting priority to real-time for os-level thread scheduling
OS_PRIORITY_BOOST = True

# Batch size for queue processing to minimize system calls
# Increasing batch size reduces CPU context switching frequency
PROCESS_BATCH_SIZE = 64

# Detection buffer settings
# Reduces coordinate calculation drift during high-speed sessions
PRECISION_THRESHOLD = 0.005

# Thread management
# Limits pool size to prevent exhaustion on lower-end hardware
MAX_WORKER_THREADS = 4

# Default event type mappings for faster lookup operations
EVENT_MAPPING = {
    'left': 1,
    'right': 2,
    'middle': 3
}

# System path normalization constants
# Using binary flags for cross-platform event polling efficiency
IS_WINDOWS = sys.platform == 'win32'
IS_LINUX = sys.platform.startswith('linux')
