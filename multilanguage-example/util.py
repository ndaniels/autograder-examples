from os.path import exists
# Checks if the string passed in is all 1's and 0's
def checkString(istring):
    success = True
    for x in range(len(istring)):
        if not (istring[x] == '1' or istring[x] == '0'):
            success = False
    return success


def getProgram():
    rust_path = "/autograder/student/huffman/target/release/huffman"
    c_path = "/autograder/student/huffman/huffman"
    python_path = "/autograder/student/huffman.py"
    # if we can find a rust impl in appropriate place, it's that
    if exists(rust_path):
        return rust_path
    elif exists(c_path):
        return c_path
    else:
        # if the python solution doesn't exist, then this will fail
        # when running the tests, which is appropriate behavior
        return "python3 " + python_path
