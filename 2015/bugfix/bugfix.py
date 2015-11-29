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
'1254',
'1405',
'1406',
'1709',
'1720',
'1778',
'2024',
'2346',
'2288',
'2300',
'2325',
'2352',
'2355',
'2377',
'2419'
]

def generate_tasks():

  for b in xrange(len(bugs)):
    title = "Investigate/Fix Bug: Ticket #" + bugs[b]
    description = "First complete one of the Getting Started tasks.<p><p>\
Investigate the bug described in Ticket #" + bugs[b] + " on\
 <a href=https://www.rtems.org/bugzilla/show_bug.cgi?id=" + bugs[b] + ">\
 [the RTEMS Trac](https://devel.rtems.org/ticket/" + bugs[b] + ")\
 Follow the [directions for this task](https://devel.rtems.org/wiki/GCI/QA/InvestigateTicket) on our wiki.
"
    max_instances = "1"	
    mentors = "\"" + str(get_mentor(year+p)) + "\""
    tags = "wiki"
    is_beginner = "true"
    categories = "\"3\""
    	# 1: Coding. 2: Documentation & Training. 3: Outreach & Research.
	# 4: Quality Assurance. 5: User Interface.
    time_to_complete = "4"
    private_metadata = "citations"

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
