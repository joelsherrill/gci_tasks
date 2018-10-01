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
  -y --year           year to generate\n\
  -p --pages          number of pages in search results for the given year\n\
"

def get_mentor(n):
  cmd = os.path.join("..","get_mentor") + " " + str(n)
  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
  (m, e) = proc.communicate()
  return m

def generate_tasks(year, pages):
  for p in xrange(pages):
    title = "\"Update Citations " + str(year) + "-" + str(p+1) + "\""
    description = "\"This task consists of updating the\
 [RTEMS References Wiki page](https://devel.rtems.org/wiki/References/" + str(year) + ") according to the instructions given in the\
 [RTEMS GCI Wiki page](https://devel.rtems.org/wiki/GCI/Outreach/Citations)\
 for the year " + str(year) +\
 " and page " + str(p+1) + ". You will need to\
 request a user account on the wiki and be careful to avoid making updates\
 that conflict or delete other relevant citations. You will upload a text\
 file containing the entries that you added to the wiki page.\
 We have constructed the\
 [Google Scholar Search for this task](http://scholar.google.com/scholar?start=" + str(p*10) +\
 "&q=RTEMS&hl=en&lr=lang_en&as_sdt=1%2C47&as_vis=1&as_ylo=" + str(year) +\
 "&as_yhi=" + str(year) +\
 ") for your convenience.\""
    max_instances = "1"	
    mentors = "\"" + str(get_mentor(year+p)) + "\""
    tags = "wiki"
    is_beginner = "true"
    categories = "\"5\""
	# 1: Coding. 2: User Interface. 3: Documentation & Training.
	# 4: Quality Assurance. 5: Outreach & Research.
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
  year = 0
  pages = 0

  # Process args
  try:
    opts, args = getopt.getopt(sys.argv[1:], "hy:p:",
        ["help", "year", "pages"])
  except getopt.GetoptError, err:
    print str(err)
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ("-h", "--help"):
      usage()
      sys.exit()
    elif opt in ("-y", "--year"):
      year = int(arg)
    elif opt in ("-p", "--pages"):
      pages = int(arg)
    else:
      usage()
      assert False, "unhandled option"

  if year == 0 or pages == 0:
    usage()
    sys.exit(0)

  emit_header()
  generate_tasks(year, pages)

if __name__ == "__main__":
  main()
