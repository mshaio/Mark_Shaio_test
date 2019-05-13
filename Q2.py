"""
Question B

The goal of this question is to write a software library that accepts 2 version
string as input and returns whether one is greater than, equal, or less than the
other. As an example: “1.2” is greater than “1.1”. Please provide all test
cases you could think of.
"""
def version_validation(string1, string2):
    """Validates string1 and string2 are valid, ie, does not contain alphabets
    and special characters.

    Args:
        string1: Version string 1, accepts a list.
        string2: Version string 2, accepts a list.

    Returns:
        The return value. True for no errors and False for invalid strings
    """
    for i in range(len(string1)):
        try:
            string1[i] = int(string1[i])
            string2[i] = int(string2[i])
        except ValueError:
            print("Version string must be digits")
            return False
    return True

def version_comparison(version1, version2):
    """Compares two 2 version strings.

    Args:
        version1: Version string 1, accepts a string.
        version2: Version string 2, accepts a string.

    Returns:
        Returns the newer version, if equal returns both are the same .
    """
    string1 = version1.split('.')
    string2 = version2.split('.')

    while len(string1) > len(string2):
        string2.append(0)
    while len(string2) > len(string1):
        string1.append(0)

    if version_validation(string1, string2) == True:
        for i in range(len(string1)):
            string1[i] = int(string1[i])
            string2[i] = int(string2[i])
            if int(string1[i]) > int(string2[i]):
                return version1
            if int(string2[i] > int(string1[i])):
                return version2
        return version1 + " is equal to " + version2

#Some tests
#First string is larger in the last element
print(version_comparison("1.2.3","1.2.1"))
print(version_comparison("1.2.3","1.2.4"))
print(version_comparison("1.2.1","1.2.2"))
#First string is larger in the first element
print(version_comparison("2.2.3","1.2.1"))
print(version_comparison("1.2.1","1.2.0"))
#Strings are different in length
print(version_comparison("1.2.3","1.2"))
print(version_comparison("2.1","1.2.1"))
#Miscellaneous
print(version_comparison("1.2.1.12.4.5","4.3"))
print(version_comparison("5.1","5.2.1.12.4.5"))
#Equal
print(version_comparison("3.2.1","3.2.1"))
#Strings containing more than just numbers, ie has alphabets or special characters
print(version_comparison("a.2","1.2.1"))
print(version_comparison("2.bc","1.2.1"))
print(version_comparison("#.2","1.2.1"))
print(version_comparison("2.1","1.*.1"))
