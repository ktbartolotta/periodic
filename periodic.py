#!/usr/bin/env python

import pprint
import re
import sys


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
				el = [r["symbol"] for r in table \
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


def main(word):

	print build_string(word)


if __name__ == "__main__":
	main(sys.argv[1])