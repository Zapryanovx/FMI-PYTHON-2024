def type_check(mode):
    """Check the types of input arguments or the output of a function."""
    
    def decorator(*expected):
        """Accept the expected types."""
        
        def wrapper(func):
            """Perform the type checking."""
            
            def validation(*args, **kwargs):
                """Validate the types of input arguments and the return the result if possible."""
                
                def expected_args_message():
                    """Generate a message listing the expected argument types."""
                    return "expected " + ", ".join([str(valid) for valid in expected]) + "!"
                
                if mode == 'in': 
                    
                    all_args = list(args) + list(kwargs.values())
                    # Check if non-valid type is found 
                    for arg in all_args:
                        if not isinstance(arg, expected):
                            print("Invalid input arguments, " + expected_args_message())
                            return func(*args, **kwargs)

                res = func(*args, **kwargs)
                
                # Check if return of function is non-valid type
                if mode == 'out' and not isinstance(res, expected):
                        print("Invalid output value, " + expected_args_message())
    
                return res  
            return validation                                           
        return wrapper
    return decorator
