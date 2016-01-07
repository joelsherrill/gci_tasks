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

pages = [
'TBR/Review/CVSPlot',
'TBR/Review/DateTimeHardwareIssues',
'TBR/Review/GSOC_F12_ToolChainSetup',
'TBR/Review/HomePage',
'TBR/Review/OASL',
'TBR/Review/RTEMS411Ideas',
'TBR/Review/Real-Time_Resources',
'TBR/Review/RsgTrialsAndTribulations',
'TBR/Review/Steering_Committee',
'TBR/Review/ToolStatus'
]

def generate_tasks():

  for b in xrange(len(pages)):
    title = "Resolve Wiki Page: " + pages[b]
    description = "\
Investigate the page located on\
 [the RTEMS Trac Wiki](https://devel.rtems.org/wiki/" + pages[b] + ")\
 Follow the [directions for this task](https://devel.rtems.org/wiki/GCI/UI/WikiTBR) on our wiki.\
"
    max_instances = "1"	
    mentors = "\"amardtakhar@gmail.com," + str(get_mentor(b)) + "\""
    tags = "\"wiki,research\""
    is_beginner = "false"
    categories = "\"2,3,4,5\""
	# 1: Coding. 2: User Interface. 3: Documentation & Training.
	# 4: Quality Assurance. 5: Outreach & Research.
    time_to_complete = "3"
    private_metadata = "TBR"

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
