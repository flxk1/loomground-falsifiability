# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 flxk1
"""loomground-falsifiability — How could this evidence be shown wrong?

One narrow problem. See :mod:`loomground_falsifiability.falsifiability` for the reasoning;
this module only re-exports it and the version.
"""

from ._version import __version__
from .falsifiability import (
    Falsifiability,
    SUPPORT_FLOOR,
    Evidence,
    rank,
    best_support,
    support_verdict,
    fold_support,
)

__all__ = [
    "__version__",
    "Falsifiability",
    "SUPPORT_FLOOR",
    "Evidence",
    "rank",
    "best_support",
    "support_verdict",
    "fold_support",
]
