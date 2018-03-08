import hashlib

phrase = raw_input("Phrase to hash: ")

sha = hashlib.sha256(phrase)

print(sha.hexdigest())
