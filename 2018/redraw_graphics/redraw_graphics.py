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

tasks = [
('rtems-docs/images/c_user/rtemsarc.png',
'SVG',
'redraw reasonably faithfully but attractively'),
('rtems-docs/images/c_user/rtemspie.png',
'SVG',
'update to reflect current managers in Classic API. Design latitude allowed'),
('rtems-docs/images/c_user/semaphore_attributes.png',
'Dot PlantUML maybe',
'redraw reasonably faithfully but attractively'),
('rtems-docs/images/c_user/states.png',
'SVG',
'redraw reasonably faithfully but attractively'),
('rtems-docs/images/networking/PCIreg.jpg',
'SVG',
'redraw reasonably faithfully but attractively'),
('rtems-docs/images/networking/networkflow.jpg',
'PlantUML',
'redraw reasonably faithfully but attractively as flowchart'),
('rtems-docs/images/networking/recvbd.jpg',
'SVG',
'redraw reasonably faithfully but attractively'),
('rtems-docs/images/user/hw-layers.png',
'SVG',
'redraw reasonably faithfully but attractively'),
('rtems-docs/images/user/rtems-trace-buffering.png',
'SVG',
'redraw reasonably faithfully but attractively'),
('rtems-docs/images/user/rtems-trace-printk.png',
'SVG',
'redraw reasonably faithfully but attractively'),
]

def generate_tasks():
  i = 0
  for t in tasks:
    title = "\"Redraw Graphics: " + t[0] + "\""
    description = "\"\
This task consists of redrawing the file " + t[0] + " in a new and open source format. For this image, use the " + t[1] + " format and " + t[2] + ".\n\
\n\
The image file is located in the [rtems-docs git repository](https://git.rtems.org/rtems-docs/tree). The file can be viewed online if you start browsing the path from https://git.rtems.org/rtems-docs/tree/images.\n\
\n\
You will submit a PNG preview of your new image and the original artwork files in the native format of " + t[1] + " output. The desired format is one of the following:\n\
- SVG\n\
- an ASCII drawing language like Graphviz/Dot or PlantUML\n\
\n\
If SVG, then you can use any number of tools such as Inkscape, which is free open-source.\n\
\n\
[Graphviz](https://www.graphviz.org/) includes dot which is a simple command language to draw graphics like flowcharts.\n\
\n\
[PlantUML](https://www.plantuml.com) is a simple command language to draw UML diagrams including inheritance, sequence, and flowcharts.\n\
\""
    max_instances = "1"	
    mentors = "\"joelsherrill@gmail.com," + str(get_mentor(i)) + "\""
    tags = "\"graphics\""
    is_beginner = "false"
    categories = "\"5\""
	# 1: Coding. 2: User Interface. 3: Documentation & Training.
	# 4: Quality Assurance. 5: Outreach & Research.
    time_to_complete = "2"
    private_metadata = "redraw"

    print(title + ", " + description + ", " + max_instances + ", " +
        mentors + ", " + tags + ", " + is_beginner + ", " + categories + ", " +
        time_to_complete + ", " + private_metadata)
    i += 1

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
