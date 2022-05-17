def is_rotation(s1, s2):
    return s2 in (s1 + s1)

s1 = 'waterbottle'
s2 = 'erbottlewat'

assert is_rotation(s1, s2)
