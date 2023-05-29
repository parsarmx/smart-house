from os import environ


# GET ENV UTIL
def get_env(key, default=None, optional=False):
    """Return environment variables with some options."""
    val = environ.get(key)
    if val is not None:
        return val
    elif default is not None:
        return default
    elif not optional:
        raise ValueError(f"Environment variable {key} was not defined")
