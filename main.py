"""
HW04 — Simple Hash Set using chaining.
Implements make_set, add, contains, remove, size.
"""

def _hash(key, m):
    """Compute a simple deterministic hash index for key."""
    return sum(ord(c) for c in key) % m

def make_set(m):
    """Return a new hash set with m empty buckets (lists)."""
    return [[] for _ in range(m)]

def add(s, key):
    """Add key to set if not present. Return True if added, False if duplicate."""
    idx = _hash(key, len(s))
    bucket = s[idx]
    if key in bucket:
        return False
    bucket.append(key)
    return True

def contains(s, key):
    """Return True if key is in set, else False."""
    idx = _hash(key, len(s))
    return key in s[idx]

def remove(s, key):
    """Remove key if present. Return True if removed, False otherwise."""
    idx = _hash(key, len(s))
    bucket = s[idx]
    if key in bucket:
        bucket.remove(key)
        return True
    return False

def size(s):
    """Return total number of stored keys in the set."""
    return sum(len(bucket) for bucket in s)

if __name__ == "__main__":
    # Manual test
    s = make_set(5)
    print(add(s, "A"))   # True
    print(add(s, "A"))   # False
    print(contains(s, "A"))  # True
    print(remove(s, "A"))    # True
    print(contains(s, "A"))  # False
    print(size(s))           # 0
