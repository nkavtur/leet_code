def is_palindromic_perm(s):
    vector = [0] * 128

    for c in s:
        if c.isalnum():
            vector[ord(c.lower())] = (vector[ord(c.lower())] + 1) % 2

    sm = sum(vector)
    return sm == 0 or sm == 1

assert is_palindromic_perm("aba") is True
assert is_palindromic_perm("aab") is True
assert is_palindromic_perm("abba") is True
assert is_palindromic_perm("aabb") is True
assert is_palindromic_perm("a-bba") is True
assert is_palindromic_perm("a-bba!") is True
assert is_palindromic_perm("Tact Coa") is True
assert is_palindromic_perm("jhsabckuj ahjsbckj") is True
assert is_palindromic_perm("Able was I ere I saw Elba") is True
assert is_palindromic_perm("So patient a nurse to nurse a patient so") is False
assert is_palindromic_perm("Random Words") is False
assert is_palindromic_perm("Not a Palindrome") is False
assert is_palindromic_perm("no x in nixon") is True
assert is_palindromic_perm("azAZ") is True
