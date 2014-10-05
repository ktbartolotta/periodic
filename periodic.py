#!/usr/bin/env python

import pprint
import re


def _get_periodic_table(file):

	table = []
	table_file = open(file)
	for row in table_file:
		t = [r for r in row.replace(
				"\t", " ").replace("\n","").split(
				" ") if r != "" and r != "*"][:4]
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
	for x in range(0, len(word), 2):
		print word[x], word[x+1] if (x+1) < len(word) else None
		


def main():

	print build_string("keith")


if __name__ == "__main__":
	main()