#!/bin/python
##
## generate GCI tasks for fixing pages
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

ideas = [
'RTEMS Test Screen Validation',
'Improve GDB Simulation',
'Simulator Updates',
'Testing of the GNU Tools',
'POSIX Compliance Test Suite',
'RTEMS Test Template',
'Fault tolerance',
'Config GUI (Python)',
'Build Variables (Python) ',
'Improve RSB (Python)',
'Python GDB Support (Python) ',
'Static Analysis of Stack Usage',
'Python Coverage Reporting (Python)',
'GCov Reports',
'GProf Reports',
'GDB Coverage',
'Improve Eclipse Plugin',
'Using clang',
'eVisual Studio',
'ArgoUML ',
'Improvements to SMP support',
'Unified Interrupts',
'Rump Kernels',
'TinyRTEMS',
'Paravirtualization',
'CPU Statistics',
'Stack Checker',
'OSEK',
'Programmable Logic Controller',
'ARINC653 in RTEMS ',
'Update the RTEMS TCP/IP stack',
'USB stack',
'Mono On RTEMS',
'Port V8 JavaScript Engine to RTEMS',
'SWIG on RTEMS',
'Internet of Things (IoT)',
'Port Monkey HTTP Server',
'Port Transparent IPC',
'Line Editor',
'Runtime Loader (RTL)',
'RTEMS Toolkits',
'LWIP',
'Rock on RTEMS'
]

def generate_tasks():

  for b in xrange(len(ideas)):
    title = "Convert Page Page to Ticket or Obsolete: " + ideas[b]
    description = "\"\
This task involves updating our [(GSoC) Open Projects](https://devel.rtems.org/wiki/Developer/OpenProjects) page for the project idea: " + ideas[b] + ".\n\
\n\
We have been slowly converting Open Project descriptions from wiki pages into tickets for projects that are still of interest, or moving uninteresting projects to the bottom of the page under the Obsolete section heading. For this task, investigate the project idea to determine whether to convert it to a ticket or to move it to the obsolete category. You may need to ask for input from the developer community to help you make this decision.  If it should become a ticket, then make the conversion to a ticket as per the instructions on the Open Projects page, and strikethrough the text. If the project idea is determined to be obsolete, move the text to the Obsolete section. \
\n\n\
You will submit what decision was made about the project idea. A mentor will verify that you have created the ticket or moved the task to Obsolete correctly. \
\""
    max_instances = "1"	
    mentors = "\"joelsherrill@gmail.com,gedarebloom@gmail.com,chrisj@rtems.org,amardtakhar@gmail.com," + str(get_mentor(b)) + "\""
    tags = "\"wiki,gsoc,trac,research\""
    is_beginner = "false"
    categories = "\"5\""
	# 1: Coding. 2: User Interface. 3: Documentation & Training.
	# 4: Quality Assurance. 5: Outreach & Research.
    time_to_complete = "4"
    private_metadata = "open"

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
