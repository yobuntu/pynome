import os
from importlib import import_module


def import_all(package):
    """Import all files recursively in dir"""
    root = import_module(package)
    package_dir = os.path.dirname(root.__file__)
    for fn in sorted(os.listdir(package_dir)):
        abs_fn = os.path.join(package_dir, fn)
        # Don't re-import root
        if fn.endswith('.py') and fn != '__init__.py':
            module = '.%s' % fn[:-3]
            import_module(module, package)
        elif os.path.isdir(abs_fn):
            if any([f.endswith('.py') for f in os.listdir(abs_fn)]):
                import_all('%s.%s' % (package, fn))
