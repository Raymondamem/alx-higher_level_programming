def magic_string():
  """Returns a string "BestSchool" n times the number of the iteration."""
  return "BestSchool" * len(magic_string.caller.frameinfo()[2])
