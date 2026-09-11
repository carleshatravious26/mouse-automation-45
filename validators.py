from typing import Tuple, Union, Any

def validate_interval(interval: Union[int, float]) -> float:
    '''
    Validates the click interval to ensure it is a positive number.

    Args:
        interval: The time delay between clicks in seconds.

    Returns:
        The validated interval as a float.

    Raises:
        TypeError: If the interval is not a number.
        ValueError: If the interval is less than or equal to zero.
    '''
    if not isinstance(interval, (int, float)):
        raise TypeError(f'Interval must be a number, got {type(interval).__name__}')
    if interval <= 0:
        raise ValueError(f'Interval must be greater than 0, got {interval}')
    return float(interval)

def validate_coordinates(coords: Tuple[Any, Any]) -> Tuple[int, int]:
    '''
    Validates the screen coordinates to ensure they are integers.

    Args:
        coords: A tuple containing (x, y) coordinate values.

    Returns:
        A tuple of validated integer coordinates.

    Raises:
        TypeError: If coordinates are not a sequence of length 2.
        ValueError: If coordinate values cannot be converted to integers or are negative.
    '''
    if not isinstance(coords, tuple) or len(coords) != 2:
        raise TypeError('Coordinates must be a tuple of (x, y)')\