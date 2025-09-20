import os

"""
Functions to read and modify environment variables.

    os.environ                          → Dictionary-like access to environment variables.
    os.getenv(key, default=None)        → Get an environment variable safely.
    os.putenv(key, value)               → Set an environment variable (not recommended; prefer os.environ).
    os.unsetenv(key)                    → Remove an environment variable.

Use case: Managing configuration for applications, accessing credentials, setting PATH.
"""


### ------------------------------------------
### Get an environment variable
### -----------------------------------------

# print(os.getenv("HOME"))  # Get the HOME environment variable
# print(os.getenv("NON_EXISTENT_VAR", "default_value"))  # Get a non-existent var with default value

# envs = ["HOME","USER","PATH","PWD"]

# for env in envs:
#     print(f"{env}: {os.getenv(env)}")
#     print()


### -----------------------------------------
### Set an environment variable
### -----------------------------------------

# os.environ["MY_VAR"] = "some_value"
# print(os.getenv("MY_VAR"))  # Get the newly set environment variable

