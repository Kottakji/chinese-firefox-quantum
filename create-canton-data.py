from bs4 import BeautifulSoup
import urllib3


def get_cantonese_characters_from_url(url):
    """
    Creates the dictionary files from the urls give from http://www.cantonese.sheik.co.uk/scripts/masterlist.htm
    As he didn't provide a dict file to use...
    :param url:
    :return:
    """
    http = urllib3.PoolManager()
    r = http.request('GET', url)

    soup = BeautifulSoup(r.data, 'html.parser')

    masterlist = soup.find('table', {'class': 'masterlist'})

    result = []

    for tr in masterlist('tr'):

        tmp = []
        last = None

        for td in tr('td'):
            c = td['class']
            if 'chinese' in c:
                tmp.append(td('a')[0].contents[0])
            if 'listjyutping' in c:
                tmp.append(' '.join(td.contents))
            if last == 'listpinyin':  # The translation comes after 'lastpinyin', but doesn't have a id...
                tmp.append(td.contents[0])
                last = None
            if 'listpinyin' in c:
                last = 'listpinyin'

        if tmp:
            result.append(tmp)

    with open('data/cantonese/new-dict.dat', 'a') as dict:

        for r in result:
            # Some characters do have simplified as optional for cantonese, so we split them into two records
            if '/' in r[0]:
                for character in str(r[0]).split(' / '):
                    dict.write('{0}\t[{1}]{2}\n'.format(character, r[1], r[2]))
            else:
                # Everything is normal, just write the line to the dict file
                dict.write('{0}\t[{1}]{2}\n'.format(r[0], r[1], r[2]))

    print('done')


def get_cantonese_words_from_url(url):
    """
    Creates the dictionary files from the urls give from http://www.cantonese.sheik.co.uk/scripts/masterlist.htm
    As he didn't provide a dict file to use...
    :param url:
    :return:
    """
    http = urllib3.PoolManager()
    r = http.request('GET', url)

    soup = BeautifulSoup(r.data, 'html.parser')

    table = soup('table')[2]

    result = []

    for tr in table('tr'):

        tmp = []

        tds = tr('td')
        try:
            if 'wl_uni' in tds[0]['class']:
                tmp.append(tds[0]('a')[0].contents[0])
                tmp.append(tds[1].get_text())
                tmp.append(tds[3].contents[0])
                result.append(tmp)
        except KeyError:
            pass  # They opening and closing part of the table are useless and don't have a class

    with open('data/cantonese/new-dict.dat', 'a') as dict:

        for r in result:
            # Some characters do have simplified as optional for cantonese, so we split them into two records
            if '/' in r[0]:
                for character in str(r[0]).split(' / '):
                    dict.write('{0}\t[{1}]{2}\n'.format(character, r[1], r[2]))
            else:
                # Everything is normal, just write the line to the dict file
                dict.write('{0}\t[{1}]{2}\n'.format(r[0], r[1], r[2]))

    print('done')


"""
# STEP 1: Fill in this list for the SINGLE CHARACTERS
urls = []

for i in range(0, 15):
    urls.append('http://www.cantonese.sheik.co.uk/scripts/masterlist.htm?action=onelevel&level=1&page={0}'.format(i))

for i in range(0, 26):
    urls.append('http://www.cantonese.sheik.co.uk/scripts/masterlist.htm?action=onelevel&level=2&page={0}'.format(i))

for i in range(0, 53):
    urls.append('http://www.cantonese.sheik.co.uk/scripts/masterlist.htm?action=onelevel&level=3&page={0}'.format(i))

for i in range(0, 14):
    urls.append('http://www.cantonese.sheik.co.uk/scripts/masterlist.htm?action=onelevel&level=4&page={0}'.format(i))

for url in urls:
    get_cantonese_characters_from_url(url)
"""


"""

# STEP 2: Fill in the list for the WORDS
urls = []

for i in range(0, 25):
    urls.append('www.cantonese.sheik.co.uk/scripts/wordlist.htm?level=1&wordtype={0}'.format(i))

for i in range(0, 191):
    urls.append('www.cantonese.sheik.co.uk/scripts/wordlist.htm?level=2&wordtype={0}'.format(i))

for i in range(0, 2207):
    urls.append('www.cantonese.sheik.co.uk/scripts/wordlist.htm?level=3&wordtype={0}'.format(i))

for i in range(0, 511):
    urls.append('www.cantonese.sheik.co.uk/scripts/wordlist.htm?level=4&wordtype={0}'.format(i))

for i in range(0, 81):
    urls.append('www.cantonese.sheik.co.uk/scripts/wordlist.htm?level=5&wordtype={0}'.format(i))

for url in urls:
    get_cantonese_words_from_url(url)

"""
"""
# STEP 3: Merge the files
read_files = ['data/cantonese/dict-old.dat', 'data/cantonese/final.dat']

with open('data/cantonese/new-dict.dat', 'wb') as final:
    for f in read_files:
        with open(f, 'rb') as read_file:
            final.write(read_file.read())
"""