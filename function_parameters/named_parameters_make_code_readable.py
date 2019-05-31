def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error: ' + error_message)
    # Imagine code here that logs our error to a database or file

first_number = 10
second_number = 5
    # This function call by itself is confusing, I have to look at the
    # definition of the error_logger function to understand it
    error_logger(45,1,True,'Second number greater than first','adding_method')

    # This function call by itself is easier to understand because I can 
    # see how the values I pass in map to the function parameters
    error_logger(error_code=45, 
                 error_severity=1,
                 log_to_db=True,
                 error_message='Second number greater than first',
                 source_module='adding_method')
