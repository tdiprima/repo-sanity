"""
Each checker is a function that takes a repo path
and returns a list of Findings. That's the contract.
"""

from checkers.env_file import check_env_file
from checkers.gitignore import check_gitignore
from checkers.api_keys import check_api_keys
from checkers.private_keys import check_private_keys
from checkers.shell_true import check_shell_true
from checkers.debug_prints import check_debug_prints
from checkers.secret_files import check_secret_files

# This is the only list you edit to add/remove checks.
ALL_CHECKERS = [
    check_env_file,
    check_gitignore,
    check_api_keys,
    check_private_keys,
    check_shell_true,
    check_debug_prints,
    check_secret_files,
]
