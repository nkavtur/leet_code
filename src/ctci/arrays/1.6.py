def compress(s):
    compressed = []
    count = 1

    for prev, current in zip([*s[:]], [*s[1:], None]):
        if current != prev:
            compressed += [prev, str(count)]
            count = 0
        count += 1

    return min(s, "".join(compressed), key=len)

assert compress("aabcccccaaa") == "a2b1c5a3"
assert compress("abcdef") == "abcdef"
assert compress("aabb") == "aabb"
assert compress("aaa") == "a3"
assert compress("a") == "a"
assert compress("") == ""
