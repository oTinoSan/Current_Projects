# csc220a3_tester.py

""" Tester for Assignment 3. """

###############################################################
# Auto Grader (See "A Generic Python Auto Grader")            #
# File: csc220a3_tester.py                                    #
# Author: Albert Chan                                         #
# Affiliation: Fayetteville State University                  #
#              Department of Mathematics and Computer Science #
# Copyright (c) 2019                                          #
# License: GPL 2.0                                            #
# Exception: compiled version of the tester and test data     #
#            files can be distributed to students without     #
#            source or showing the license                    #
###############################################################

import sys

MODULE = 'csc220a3'
FUNCTION = 'evaluate'
MAXSCORE = 15
TESTDATA = 'csc220a3_testdata'

def load_function(module, file_path, function='main'):
    """ Load a function from a module.
        Input: module - the module
               file_path - the path to the module
               function - the name of the function to load
        Output: the loaded function
    """
    sys.path.insert(0, file_path)
    try:
        return getattr(__import__(module), function)
    finally:
        sys.path.pop(0)

def message(record, msg, verbose):
    """ Display a message if wanted.
        Input: record - record mechanism
               msg - the message
               verbose - control whether the messsage will be display
        Output: None
    """
    if verbose:
        record(msg)

def convert_to_tuple(value):
    """ Convert value to tuple.
        Input: value - the value
        Output: the value converted to tuple
    """
    return value if isinstance(value, tuple) else (value,)

def check_exceptions(testcase, resulting_exception, verbose, record):
    """ Check for exception.
        Input: testcase - the testcase
               resulting_exception - the resulting exception
               verbose - True if wanted verbose message
               record - recording mechanism
        Output: True if passed, False otherwise
    """
    # pylint: disable = C0301
    tc_id = testcase[0]
    expected_exception = None
    if len(testcase) > 3:
        expected_exception = testcase[3]

    if expected_exception is None:
        if resulting_exception is None:
            return True
        message(record, f'TC {tc_id} failed - exception {type(resulting_exception).__name__} caught', verbose)
        return False

    if resulting_exception is None:
        message(record, f'TC {tc_id} failed - expecting an exception, none raised', verbose)
        return False

    if isinstance(resulting_exception, expected_exception):
        return True
    message(record, f'TC {tc_id} failed - unexpected exception {type(resulting_exception).__name__} caught', verbose)
    return False

def check_return_value(testcase, actual_result, verbose, record):
    """ Check for result.
        Input: testcase - the testcase
               actual_result - the result
               verbose - True if wanted verbose message
               record - recording mechanism
        Output: True if passed, False otherwise
    """
    # pylint: disable = C0301, R0911
    tc_id = testcase[0]
    expected_result = testcase[2]
    if expected_result is None:
        if not actual_result is None:
            message(record, f'TC {tc_id} failed - not expecting a return value, got {repr(actual_result)} instead', verbose)
            return False
        return True

    if actual_result is None:
        message(record, f'TC {tc_id} failed - expecting {repr(expected_result)}, got nothing', verbose)
        return False

    actual_result = convert_to_tuple(actual_result)
    expected_result = convert_to_tuple(expected_result)
    if len(actual_result) == len(expected_result) == 1:
        if actual_result[0] == expected_result[0]:
            return True
        message(record, f'TC {tc_id} failed - expecting {repr(expected_result [0])}, got {repr(actual_result [0])} instead', verbose)
        return False

    actual_length = len(actual_result)
    expected_length = len(expected_result)
    if actual_length == expected_length:
        for index in range(actual_length):
            if not actual_result[index] == expected_result[index]:
                message(record, f'TC {tc_id} failed - expecting {repr(expected_result [index])} at position {index}, got {repr(actual_result [index])} instead', verbose)
                return False
        return True
    message(record, f'TC {tc_id} failed - expecting a sequence of {len(expected_result)} values, got a sequence of {len(actual_result)} instead', verbose)
    return False

def run_single_test(function, testcase, verbose=False, record=print):
    """ Run a single testcase.
        Input: function - the function to call
               testcase - the testcase
               verbose - True if wanted verbose message (default to False)
               record - recording mechanism (default to print)
        Output: True if passed, False otherwise
    """
    test_input = convert_to_tuple(testcase[1])
    result = None
    resulting_exception = None

    try:
        result = function(*test_input)
    except Exception as err: # pylint: disable = W0703
        resulting_exception = err

    if check_exceptions(testcase, resulting_exception, verbose, record):
        if check_return_value(testcase, result, verbose, record):
            message(record, 'TC %d passed' % testcase[0], verbose)
            return True
        return False
    return False

def run_all_tests(test_suite, module=MODULE, path='.', record=print):
    """ Run all testcase.
        Input: test_suite - the testcases
               module - the module (default to MODULE defined above)
               path - the path of the module (default to current folder)
               record - recording mechanism (default to print)
        Output: score of running the testcases
    """
    # pylint: disable = C0301
    try:
        function = load_function(module, path, FUNCTION)
    except Exception as _: # pylint: disable = W0703
        record('File loading error - testing not executed.')
        return 0
    passed = []
    failed = []
    number_of_testcases = len(test_suite)
    for testcase in test_suite:
        success = run_single_test(function, testcase, False, record)
        if success:
            passed.append(testcase[0])
        else:
            failed.append(testcase[0])

    number_of_passed_testcases = len(passed)
    test_score = float(MAXSCORE) * number_of_passed_testcases / number_of_testcases
    record(f'Passed: {passed} - total {len(passed)}.')
    record(f'Failed: {failed} - total {len(failed)}.')
    record(f'\n{number_of_passed_testcases} of {number_of_testcases} testcases passed. Score = {test_score:.2f} of {MAXSCORE:.2f}.')
    return test_score

def run_testcase(tc_id, module=MODULE, path='.', record=print):
    """ Run a single testcase selected by testcase id.
        Input: tc_id - the testcase id
               module - the module (default to MODULE defined above)
               path - the path of the module (default to current folder)
               record - recording mechanism (default to print)
        Output: None
    """
    try:
        function = load_function(module, path, FUNCTION)
    except Exception as _: # pylint: disable = W0703
        record('File loading error - testing not executed.')
        return
    for testcase in TESTS:
        if testcase[0] == tc_id:
            run_single_test(function, testcase, True, print)

TESTS = load_function(TESTDATA, '.', 'TESTS')

if __name__ == '__main__':
    run_all_tests(TESTS)
