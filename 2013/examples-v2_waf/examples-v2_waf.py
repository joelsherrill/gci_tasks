#!/bin/python
##
## generate GCI tasks for updating citations
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
  if m == "gedare" or m == "chrisjohns": ## FIXME: HACK for these tasks only!
    return get_mentor(n+1)
  return m

directories = [
'misc/applib'
]

def generate_tasks():

  for d in xrange(len(directories)):
    title = "Waf conversion: Convert examples-v2/" + directories[d]
    description = "First complete one of the Getting Started tasks.\
<p><p>\
This task assists the effort of converting the build system\
 for the RTEMS examples-v2.git repository of sample applications from\
 using a set of custom Makefiles to using Waf.\
 Follow the instructions given in the\
 <a href=http://wiki.rtems.org/wiki/index.php/GoogleCodeInProjects#Convert_RTEMS_Example_Applications_to_Waf_builds>\
 RTEMS GoogleCodeInProjects Wiki page</a> for the directory: examples-v2/" +\
 directories[d] + ". You will upload a patch\
 file containing the modifications you make. Optionally you may also\
 submit your work as a pull request on GitHub.\
"
    time_to_complete = "72"
    mentors = "\"gedare,chrisjohns, " + str(get_mentor(d)) + "\""
    type = "Code"
    tags = "\"python,waf,make,git\""

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
