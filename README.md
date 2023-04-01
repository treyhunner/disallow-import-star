# Stop your users from doing whatever they want

[![PyPI - Version](https://img.shields.io/pypi/v/disallow-import-star.svg)](https://pypi.org/project/disallow-import-star)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/disallow-import-star.svg)](https://pypi.org/project/disallow-import-star)

Are you a meanie?
Do you feel your users shouldn't be allowed to to use `from your_module import *` whenever they want?

This is the package for you!

Just `pip install disallow-import-star` and add this magical lines to your module:

```python
from disallow_import_star import __all__
```

## Would you like to impose your will on *other* packages?

If you really want your users to stop using `import *` in *other* their packages, you can monkey patch your user's favorite packages, like this:

```python
from disallow_import_star import __all__
import math
import numpy
import tkinter


# Why should our users be able to use import * ANYWHERE?
math.__all__ == __all__
numpy.__all__ == __all__
tkinter.__all__ == __all__
```

## Want to control *all* the packages?

To really upset your `import *`-using users, run this:

```python
from disallow_import_star

disallow_import_star.disallow_import_star_EVERYWHERE()
```
