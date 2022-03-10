def is_unique_ascii(s):
    if len(s) > 128:
        return False

    seen = [False] * 128
    for char in s:
        if seen[ord(char)]:
            return False
        seen[ord(char)] = True

    return True


assert is_unique_ascii('abcd') is True
assert is_unique_ascii('abcda') is False
assert is_unique_ascii('') is True


def is_unique_sorting(s):
    sorted_string = sorted(s)

    prev = None
    for next in sorted_string:
        if next == prev:
            return False
        prev = next

    return True


assert is_unique_sorting('abcd')
assert is_unique_sorting('abcda') is False
assert is_unique_sorting('медведь') is False
