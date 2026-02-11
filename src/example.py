from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def m() -> Iterable:
    """Magic function."""
    return "Hello Word"
