#!/bin/python
##
## generate GCI tasks for updating citations
##

import getopt
import os
import sys

def usage():
  print "\
Usage: citations.py -[hy:p:]\n\
  -h --help           print this help\n\
  -y --year           year to generate\n\
  -p --pages          number of pages in search results for the given year\n\
"

def get_mentor(n):
  mentors = []
  mentors.append("joel_sherrill")
  mentors.append("jenniferaverettoarcorp")
  mentors.append("chrisjohns")
  mentors.append("gedare")
  return mentors[n % len(mentors)]

def generate_tasks(year, pages):
  for p in xrange(pages):
    title = "Update Citations " + str(year) + "-" + str(p+1)
    description = "This task consists of updating the\
 <a href=\"http://wiki.rtems.org/wiki/index.php/RTEMSReferences\">RTEMS\
 References Wiki page</a> according to the instructions given in the\
 <a href=\"http://wiki.rtems.org/wiki/index.php/GoogleCodeInProjects#Update_List_of_Citations\">\
 RTEMS GoogleCodeInProjects Wiki page</a> for the year " + str(year) +\
 " and page " + str(p+1) + ". You will need to\
 request a user account on the wiki and be careful to avoid making updates\
 that conflict or delete other relevant citations. You will upload a text\
 file containing the entries that you added to the wiki page.\
 We have constructed the\
 <a href=\"http://scholar.google.com/scholar?start=" + str(p*10) +\
 "q=RTEMS&hl=en&lr=lang_en&as_sdt=1,47&as_vis=1&as_ylo=" + str(year) +\
 "&as_yhi=" + str(year) +\
 "\">Google Scholar search for this task</a> for your convenience."
    time_to_complete = "72"
    mentors = get_mentor(year+p)
    type = "Outreach/Research"
    tags = "wiki"

    print(title + ", " + description + ", " + time_to_complete + ", " + 
        mentors + ", " + type + ", \"" + tags + "\"")

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

  generate_tasks(year, pages)

if __name__ == "__main__":
  main()
