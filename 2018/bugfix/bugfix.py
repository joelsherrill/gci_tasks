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
Usage: bugfix.py -[hy:p:]\n\
  -h --help           print this help\n\
"

def get_mentor(n):
  cmd = os.path.join("..","get_mentor") + " " + str(n)
  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
  (m, e) = proc.communicate()
  return m

bugs = [
'1405',
'1406',
'2024',
'2581',
'1778',
'2562',
'3450',
'2087',
'2189',
'2541',
'2860'
]

def generate_tasks():

  for b in xrange(len(bugs)):
    title = "Investigate/Fix Bug: Ticket #" + bugs[b]
    description = "\"First complete one of the Getting Started tasks.\
 \
 Investigate the bug described in Ticket #" + bugs[b] + " on\
 [the RTEMS Trac](https://devel.rtems.org/ticket/" + bugs[b] + ")\
 Follow the [directions for this task](https://devel.rtems.org/wiki/GCI/QA/InvestigateTicket) on our wiki.\
 \
 The outcome of this task will be a comment on the ticket to suggest a path forward.\
 If a bug fix is available you may be expected to test the fix and possibly produce an updated patch.\
\""
    max_instances = "1"	
    mentors = "\"joelsherrill@gmail.com,gedarebloom@gmail.com," + str(get_mentor(b+2)) + "\""
    tags = "\"c,debugging\""
    is_beginner = "false"
    categories = "\"1,3,4\""
	# 1: Coding. 2: User Interface. 3: Documentation & Training.
	# 4: Quality Assurance. 5: Outreach & Research.
    time_to_complete = "5"
    private_metadata = "bugfix"

    print(title + ", " + description + ", " + max_instances + ", " +
        mentors + ", " + tags + ", " + is_beginner + ", " + categories + ", " +
        time_to_complete + ", " + private_metadata)

def emit_header():
    print("name,description,max_instances,mentors,tags,is_beginner,categories,time_to_complete_in_days,private_metadata")
    return

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

  emit_header()
  generate_tasks()

if __name__ == "__main__":
  main()
