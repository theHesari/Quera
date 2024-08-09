print(' '.join(sorted([char if (ord(char) - 97) % 2 == 0 else char.upper() for char in str(input()).strip()], reverse=True)))
