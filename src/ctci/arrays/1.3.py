def urlify(s, actual_len, pattern='%20'):
    chars = [c for c in s]

    i = len(s) - 1
    for k in reversed(range(actual_len)):
        if chars[k] == ' ':
            i -= len(pattern) - 1
            chars[i: i+3] = '%20'
        else:
            chars[k], chars[i] = chars[i], chars[k]
        i -= 1

    return ''.join(chars)


print(urlify('Mr  John Smith      ', 14))
