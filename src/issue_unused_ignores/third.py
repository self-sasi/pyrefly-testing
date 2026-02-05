# this file should be modified when 
# `pyrefly check --remove-unused-ignores` is run
# as the ignore in this file is UNUSED.
def third(x: int) -> int:
    # this is an unused ignore
    # why? cuz `x + 1` is not a type violation
    # and pyrefly won't flag it in first place
    return x + 1  # pyrefly: ignore