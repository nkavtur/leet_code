import collections


def check_permutation_sorting(s1, s2):
    if len(s1) != len(s2):
        return False

    sorted1, sorted2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if sorted1[i] != sorted2[i]:
            return False

    return True


assert check_permutation_sorting('abc', 'bca')
assert not check_permutation_sorting('abcda', 'bcad')
assert check_permutation_sorting('abcda', 'bcada')


def check_permutation_hashtable(s1, s2):
    if len(s1) != len(s2):
        return False

    counts = collections.defaultdict(int)
    for i in range(len(s1)):
        counts[s1[i]] += 1
        counts[s2[i]] -= 1

    for _, count in counts.items():
        if count != 0:
            return False

    return True


assert check_permutation_hashtable('abc', 'bca')
assert not check_permutation_hashtable('abcda', 'bcad')
assert check_permutation_hashtable('abcda', 'bcada')
