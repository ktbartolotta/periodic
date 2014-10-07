#!/usr/bin/env python

import pprint
import re


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

	table = _get_periodic_table("periodic_table.txt")
	def build(word_, match):
		for length in xrange(2, 0, -1):
			if len(word_) >= length: 
				el = [r["symbol"] for r in table \
					if r["symbol"].upper() == word_[:length].upper()]
				if len(el) > 0:
					match.append(el[0])
					match.append(build(word_[length:], match))

		return match

	return build(word,[])			


def main():

	print build_string("pasta")


if __name__ == "__main__":
	main()