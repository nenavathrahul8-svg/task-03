def check_anagram(s1,s2):
    s1_list = sorted(s1)
    s2_list = sorted(s2)
    return s1_list == s2_list
string1 = "listen"
string2 = "silent"

print(sorted(string1))
print(sorted(string2))
print(check_anagram(string1,string2))