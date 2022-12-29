sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'
sentence = sentence.lower()



lst = ["a", "e", "i", "o", "u", "y"]
souhlasky = 0
samohlasky = 0

for i in sentence:
    if not i.isalpha():
        continue
    if i in lst:
        samohlasky = samohlasky + 1
    else:
        souhlasky = souhlasky + 1

print("souhlasky:", souhlasky)
print("samohlasky:", samohlasky)