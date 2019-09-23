
varWillbeHidden = 1  # will not be imported
varImportScopeTest = 2
varWillNotBeimported = 3  # not imported because not in __all__ list.
__all__ = ['varImportScopeTest']

def test():
    pass

