#!/usr/bin/env python

import pprint


def _get_periodic_table(file):

    table = []
    table_file = open(file)
    for row in table_file:
        t = row.split(",")
        table.append(
            {
                "atomic_no": t[0],
                "atomic_wt": t[1],
                "name": t[2],
                "symbol": t[3]
            }
        )

    return table


def build_string(word):

    matches = []
    table = _get_periodic_table("periodic_table.txt")

    def build(word_, match):
        for length in xrange(2, 0, -1):
            if len(word_) >= length:
                el = [r["symbol"] for r in table
                      if r["symbol"].upper() == word_[:length].upper()]
                if len(el) > 0:
                    matched = list(match + el)
                    if "".join(matched).upper() == word.upper():
                        matches.append(matched)
                        return
                    else:
                        build(word_[length:], matched)

        return
    build(word, [])
    return matches


def get_periodics(word):

    table = _get_periodic_table("periodic_table.txt")
    matches = build_string(word)
    periodics = []
    if len(matches) > 0:
        for match in matches:
            m = []
            for el in match:
                m += [r for r in table if r["symbol"] == el]
            periodics.append(m)

    return periodics


def main(word):

    print build_string(word)


if __name__ == "__main__":
    pprint.pprint(get_periodics("bacon"))
