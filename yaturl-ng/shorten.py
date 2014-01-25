#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


# TODO timeit
# http://stackoverflow.com/questions/742013/how-to-code-a-url-shortener

# Generate a [0-9a-zA-Z] string
#~ALPHABET = map(str, range(0, 10)) + map(chr, range(97, 123) + range(65, 91))
ALPHABET = map(str, range(0, 10)) + map(chr, range(97, 123))


def encode_id(id_number, alphabet=ALPHABET):
    """Convert an integer to a string."""
    if id_number == 0:
        return alphabet[0]

    alphabet_len = len(alphabet) # Cache

    result = ''
    c = 0
    while id_number > 0:
        c += 1
        id_number, mod = divmod(id_number, alphabet_len)
        result = alphabet[mod] + result

    print c

    return result


if __name__ == '__main__':
    print encode_id(14567)
    print encode_id(131)
    print encode_id(1352)
    print encode_id(13528)
    print encode_id(16528)
    print encode_id(63528)
    print encode_id(443528)
    print encode_id(993523428)
    print encode_id(993528)
