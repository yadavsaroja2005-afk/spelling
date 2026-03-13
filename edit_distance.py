# Recursive Python program to find minimum number of
# operations required to convert str1 to str2

def editDistance(str1, str2, m, n):

    # If first string is empty, insert all characters of second string
    if m == 0:
        return n

    # If second string is empty, remove all characters of first string
    if n == 0:
        return m

    # If last characters are the same, ignore them
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)

    # If last characters are different, consider three operations
    return 1 + min(
        editDistance(str1, str2, m, n-1),     # Insert
        editDistance(str1, str2, m-1, n),     # Remove
        editDistance(str1, str2, m-1, n-1)    # Replace
    )


# Driver code
str1 = "sunday"
str2 = "saturday"

result = editDistance(str1, str2, len(str1), len(str2))

print("Edit Distance is:", result)
