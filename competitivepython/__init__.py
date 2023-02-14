"""
The `competitivepython` package provides various algorithms and data structures
commonly used in competitive programming.

Subpackages:
- `searches`: contains search algorithms
- `graphs`: contains graph algorithms
- `sorting`: contains sorting algorithms
- `trees`: contains tree data structures and algorithms
"""

__version__ = "0.1.0"

# import subpackages
from . import searches
from . import graphs
from . import sorting
from . import trees

# make submodules available at top level (optional)
from .searches import *
from .graphs import *
from .sorting import *
from .trees import *
