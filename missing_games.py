#!/usr/bin/env python3
import sys

def main():
  if len(sys.argv) != 3:
    print("Usage: {prog} file_to_filter reference_file".format(
      prog=sys.argv[0]))
    return

  fname = sys.argv[1]
  ffile = open(fname, 'r')
  print("Opened file to filter: {0}".format(fname))
  rname = sys.argv[2]
  rfile = open(rname, 'r')
  print("Opened reference file: {0}".format(rname))

  rset = set()
  for line in rfile:
    rset.add(line.rstrip())

  for line in ffile:
    str = line.rstrip()
    app_id = str.split(',')[0]
    if app_id  not in rset:
      print(str)

  ffile.close()
  rfile.close()


if __name__ == '__main__':
  main()
