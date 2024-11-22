class ProtectedSection:
    """Handle specific exceptions in a controlled manner."""
    
    def __init__(self, log=(), suppress=()):
        self.log = log
        self.suppress = suppress
        self.exception = None
        
    def __enter__(self):
        self.exception = None
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            if exc_type in self.log:
                self.exception = exc_val
                return True
            elif exc_type in self.suppress:
                return True
        return False
    
print(None in [])