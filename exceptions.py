class MouseAutomationError(Exception):
    """Base class for exceptions in mouse automation."""
    pass

class InvalidClickLocationError(MouseAutomationError):
    """Exception raised for invalid click locations."""
    def __init__(self, message='Click location is out of bounds.'): 
        self.message = message 
        super().__init__(self.message)

class ClickNotPossibleError(MouseAutomationError):
    """Exception raised when a click cannot be performed."""
    def __init__(self, message='Click action cannot be performed at this time.'): 
        self.message = message 
        super().__init__(self.message)

class MouseAutomation:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def validate_click(self, x, y):
        if x < 0 or x >= self.screen_width or y < 0 or y >= self.screen_height:
            raise InvalidClickLocationError()

    def click(self, x, y):
        self.validate_click(x, y)
        # Simulate click action here
        # raise ClickNotPossibleError() if needed
        print(f'Clicked at ({x}, {y}')

    def perform_click(self, x, y):
        try:
            self.click(x, y)
        except MouseAutomationError as e:
            print(f'Error: {e.message}')