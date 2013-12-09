#!/bin/python
##
## generate GCI tasks for fixing bugs
##

import getopt
import sys
import os
import subprocess

def usage():
  print "\
Usage: citations.py -[hy:p:]\n\
  -h --help           print this help\n\
"

def get_mentor(n):
  cmd = os.path.join("..","get_mentor") + " " + str(n)
  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
  (m, e) = proc.communicate()
  return m

bugs = [
'1761',
'1960',
'1194',
'1321',
'1343',
'1548',
'1706',
'1987',
'2037',
'2067',
'2144',
'1309',
'1735',
'1279',
'355',
'1168',
'1323',
'1300',
'1360',
'1638',
'1640',
'1974',
'1976',
'1201',
'1785',
'1361'
]

def generate_tasks():

  for b in xrange(len(bugs)):
    title = "Investigate/Fix Bug: PR " + bugs[b]
    description = "First complete one of the Getting Started tasks.<p><p>\
Investigate the bug described in PR" + bugs[b] + " on\
 <a href=https://www.rtems.org/bugzilla/show_bug.cgi?id=" + bugs[b] + ">\
 the RTEMS Bugzilla.</a><p><p>\
 If the bug has no existing test case then implement a new test case\
 within an appropriate subdirectory of testsuites and submit the patches\
 here and on the Bugzilla. If the bug affects functionality that is already\
 tested by an existing test case then extend that test case to check for the\
 conditions of the reported bug (if the test for the bug does not exist).<p><p>\
 If the bug has already been fixed make a comment on the Bugzilla to that\
 effect and upload an empty file here.\
 If the bug has a fix you can implement then write the fix and submit any\
 patches to the RTEMS Bugzilla and to Melange.\
 If the bug is not fixed and is beyond your abilities then write a brief report\
 describing the bug behavior and possible fixes. Submit the report here on\
 Melange and also make a comment on the RTEMS Bugzilla.\
"
    time_to_complete = "72"
    mentors = str(get_mentor(b))
    type = "Code"
    tags = "\"c,debugging\""

    print(title + "," + description + "," + time_to_complete +
        "," + mentors + "," + type + "," + tags)

def main():
  # default args

  # Process args
  try:
    opts, args = getopt.getopt(sys.argv[1:], "h",
        ["help"])
  except getopt.GetoptError, err:
    print str(err)
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    else:
      usage()
      assert False, "unhandled option"

  generate_tasks()

if __name__ == "__main__":
  main()
