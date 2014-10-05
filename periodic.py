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
	match = []
	def build(word):
		el = [r for r.symbol in table if r.symbol == word[:2]]
		if len(el) > 0:
			match.append([el])
			match.append(build(word[2:]))
		else:
			el = r for r.symbol in table if r.symbol == word[:1]]
			if len(el) > 0:
				match.append([el])
				match.append(build(word[1:]))
			


def main():

	#print build_string("keith")
	pprint.pprint(_get_periodic_table("periodic_table.txt"))


if __name__ == "__main__":
	main()