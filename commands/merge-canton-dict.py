import re


def merge_canton_dict():
    """
    After creating the cantonese dictionary, many entries are missing.
    Therefore, for each word in the mandarin dict that isn't in the cantonese dict, add it
    Note: this takes a few hours
    :return:
    """
    final = open('data/cantonese/final.dat', 'w')

    with open('data/dict.dat', 'r') as mandarin_dict:
        for line in mandarin_dict.readlines():
            char = line.split(' ')[0]
            if len(char) > 1:

                skip = False  # In case it is already found

                # Do we need this one translated? Check if it already exists
                with open('data/cantonese/dict.dat', 'r') as cantonese_dict:
                    for cantonese_line in cantonese_dict.readlines():
                        split = cantonese_line.split('\t')
                        if char == split[0]:
                            skip = True
                            continue

                if skip:
                    continue

                tmp = []  # Store the cantonese info for each character

                for c in char:
                    if re.match('[\u4E00-\u9FCC]', c):
                        with open('data/cantonese/dict.dat', 'r') as cantonese_dict:
                            for cantonese_line in cantonese_dict.readlines():
                                split = cantonese_line.split('\t')
                                if c == split[0]:
                                    # Found the character as an exact match, now we want to store the cantonese pinyin
                                    # But some single characters have multiple pronunciations
                                    regex_result = re.search('\[(.+?)\]', cantonese_line)
                                    pinyin = regex_result.group(1)
                                    tmp.append(pinyin.split()[0])  # As I don't speak Cantonese, assume the first one
                                    break  # The first one found is of higher quality

                if tmp:
                    translation = (re.search('\](.+)', line).group(1)[2:-1])
                    translation = translation.split('/CL:', 1)[0]  # Don't bother with the CL (measurewords)

                # Add only if all characters were translatable
                if len(tmp) == len(char):
                    final.write('{0}\t[{1}]{2}\n'.format(char, ' '.join(tmp), translation))

    final.close()


# merge_canton_dict()
