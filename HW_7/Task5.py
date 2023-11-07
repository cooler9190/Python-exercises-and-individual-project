# 5. Longest Common Prefix
# Description: Write a function
# that finds the longest
# common prefix string
# amongst an array of strings.
# Example
# Input: ["flower", "flow", "flight"]
# Example
# Output: "fl"

def longest_common_prefix(string_list):
    longest_prefix = ''
    string_list.sort()

    for i in range(len(string_list)):
        for j in range(i, len(string_list)):
            longest_prefix = set(string_list[i]) & set(string_list[j])

    longest_prefix = str(longest_prefix)

    return longest_prefix


if __name__ == '__main__':
    new_list = ['flower', 'flow', 'flight']

    print(longest_common_prefix(new_list))
