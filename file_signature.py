import sys
from config import signatures, bcolors

signatures = signatures.signatures

with open(sys.argv[1],"rb") as fp:
    fp = fp.read()
    hex_list = ["{:02x}".format(c).upper() for c in fp]

candidates = []
candidate_found = False
for signature in signatures:
    if signature["hex"].split(" ")[0] == hex_list[0]:
        candidate_found = True
        candidates.append(signature["ascii"])

candidate_lengths = []
candidate_ascii = []
for candidate in candidates:
    for signature in signatures:
        if candidate == signature["ascii"]:
            i = 0
            candidate_count = 0
            this_hex = []
            for hex_part in signature["hex"].split(" "):
                if hex_part == hex_list[i]:
                    candidate_count += 1
                    this_hex.append(hex_part)
                else:
                    break
                i += 1
            candidate_lengths.append(candidate_count)
            candidate_ascii.append(signature["ascii"])
            # print(signature["file_extension"], this_hex[:i], signature["hex"].split(" "))
            # if " ".join(this_hex[:i]) in " ".join(signature["hex"].split(" ")) and candidate_count == len(this_hex[:i]):
            #     candidate_found = True
            #     print("File signature match found!")
            #     print("ASCII: " + signature["ascii"])
            #     print("File Type: " + signature["file_extension"])
            #     print("Description: " + signature["description"])

max_length = max(candidate_lengths)
max_ascii = candidate_lengths.index(max(candidate_lengths))
file_extensions = []
description = ""
for signature in signatures:
    if signature["ascii"] == candidate_ascii[max_ascii]:
        file_extensions.append(signature["file_extension"])
        description = signature["description"]
print(bcolors.CWHITE + "Potential file signature(s) for " + bcolors.CVIOLET + str(sys.argv[1]) + bcolors.CWHITE + " found!")
print("File extension(s): " + bcolors.CVIOLET + ", ".join(file_extensions) + bcolors.CWHITE)
print("Description: " + bcolors.CVIOLET + description + bcolors.CWHITE)