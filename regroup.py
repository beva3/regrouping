
def frecancy_characters(string):
    """
    Regroup characters by their type.
    """
    groups = {}
    for c in string:
        if c in groups:
            groups[c] += 1
        else:
            groups[c] = 1
    return groups

def regroup_characters(string):
    """
    Regroup characters by their type : voyels, consonants, digits, special characters.
    """
    groups = {
        "voyels"    : [],
        "consonants": [],
        "digits"    : [],
        "special"   : []
    }
    voyels_set = set("aeiouyAEIOUY")
    consonants_set = set("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ")
    digits_set = set("0123456789")
    special_set = set("!@#$%^&*()_+-=[]{}|;':,.<>?/")
    for c in string:
        if c in voyels_set:
            if c not in groups["voyels"]:
                groups["voyels"].append(c)
        elif c in consonants_set:
            if c not in groups["consonants"]:
                groups["consonants"].append(c)
        elif c in digits_set:
            if c not in groups["digits"]:
                groups["digits"].append(c)
        else:
            if c not in groups["special"]:
                groups["special"].append(c)
    return groups 


# Test 1
# g = frecancy_characters("helloworld")
# print(g)
# print(len(g))

# Test 2
g = regroup_characters("helloworld12354hdgd!@#$")
print(g)