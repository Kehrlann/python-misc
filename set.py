from timeit import timeit

def add_to_set(set: list, entry: str):
  key = int.from_bytes(entry.encode(), byteorder='big') % 1000
  if set[key] is None:
    set[key] = [entry]
  else:
    set[key].append(entry)
  

def contains(set: list, entry: str):
  key = int.from_bytes(entry.encode(), byteorder='big') % 1000
  if set[key] is None:
    return False
  else:
    return entry in set[key]

def setup(number):
  s = [None]*1000
  for x in range(number):
    add_to_set(s, str(x))
  return s

if __name__ == "__main__":
  print(timeit("'alpha' in set", setup="set = [str(x) for x in range(1_000_000)]", number=100))
  print(timeit("contains(s, 'alpha')", setup="s = setup(1_000_000)", number=100, globals=globals()))