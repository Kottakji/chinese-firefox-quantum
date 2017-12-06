import re

"""
I used this simple python file to convert the old dict.idx to a new dict.idx
Keeping in in case we might need it again
The numbers were off, so I had to convert the data file from the chrome version. Somehow, the line number needed to be
 substracted from the original number to get the good number. 
Uncomment the first part and run it to create the file including duplicates. Check it if looks fine, then run the other.
"""


"""  
# First function to transform the dict file
new_file = open("data/dict-new.idx", "w")
      
for line in open("data/dict.idx").read().splitlines():
    result = re.match(r'(.+)・(.+)\：(.+)', line)

    # Find the file name in the dict.dat

    for nr, l in enumerate(open("data/dict.dat").read().splitlines()):
        regex = re.compile(result.group(1) + " " + result.group(2))
        res = regex.match(l)
        if res:
            print("FOUND", result.group(1))
            print("line", l)
            print("nr", nr)

            new_file.write(result.group(1) + "・" + result.group(2) + "：" + str(int(result.group(3)) - nr) + "\n")

new_file.close()
"""


"""
# Second function to update the transformed dict file
final_file = open("data/dict-final.idx", "w")

lastGroup1 = None
lastGroup2 = None
lastGroup3 = None

for line in open("data/dict-new.idx").read().splitlines():  # TODO change test to new
    result = re.match(r'(.+)・(.+)\：(.+)', line)

    print("Doing: ", line)

    # If it was the same as the last group, but with just an increased value of 1, delete it
    if (lastGroup1 == result.group(1)) and (lastGroup2 == result.group(2)) and \
            ((int(lastGroup3) - int(result.group(3)) == 1) or (int(lastGroup3) - int(result.group(3) == -1))) is True:
        pass  # don't write it
    else:
        # Make sure to write the one with the lowest value
        if lastGroup3 and int(lastGroup3) < int(result.group(3)):
            final_file.write(lastGroup1 + "・" + lastGroup2 + "：" + lastGroup3 + "\n")
        else:
            final_file.write(line + "\n")

    lastGroup1 = result.group(1)
    lastGroup2 = result.group(2)
    lastGroup3 = result.group(3)

final_file.close()
"""
