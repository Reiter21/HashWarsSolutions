import collections
def canConstruct(ransomNote, magazine):
    return not collections.Counter(ransomNote) - collections.Counter(magazine)

for _ in range(int(input())):
    mag = input()
    note = input()
    print("YES" if canConstruct(note, mag) else "NO")