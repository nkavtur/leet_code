def are_same(s1, s2):
    i, j = 0, 0
    edits = 0

    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            edits += 1
            if len(s1) == len(s2):
                i += 1
                j += 1
            elif len(s1) < len(s2):
                j += 1
            else:
                i += 1

    while i < len(s1):
        i += 1
        edits += 1

    while j < len(s2):
        j += 1
        edits += 1

    return edits in (0, 1)

assert are_same('abc', 'abc') == True
assert are_same('abc', 'ab') == True
assert are_same('ab', 'abc') == True
assert are_same('abc', 'abd') == True
assert are_same('abcd', 'abej') == False

assert are_same("pale", "pale") == True
assert are_same("", "") == True
assert are_same("pale", "ple") == True
assert are_same("ple", "pale") == True
assert are_same("pales", "pale") == True
assert are_same("ples", "pales") == True
assert are_same("pale", "pkle") == True
assert are_same("paleabc", "pleabc") == True
assert are_same("", "d") == True
assert are_same("d", "de") == True
assert are_same("pale", "bale") == True
assert are_same("a", "b") == True
assert are_same("pale", "ble") == False
assert are_same("pale", "bake") == False
assert are_same("pale", "pse") == False
assert are_same("pale", "pas") == False
assert are_same("pas", "pale") == False
assert are_same("pkle", "pable") == False
assert are_same("pal", "palks") == False
assert are_same("palks", "pal") == False
assert are_same("ale", "elas") == False
