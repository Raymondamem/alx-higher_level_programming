#!/usr/bin/python3

mport sys
def safe_print_integer_err(value):
 """Prints an in integer with "{:d}".format().
    If a ValueError message is caught, and corresponding
    message is printed to standard error.
    Args:
        value (int): integer.
    Returns:
        If a TypeErr - False Otherwise - True.
    """
 try:
  print("{:d}".format(value))
  return (True)
 except (TypeError, ValueError):
  print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
  return (False)
