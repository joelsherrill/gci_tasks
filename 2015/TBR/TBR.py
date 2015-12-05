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
'TBR/Delete/Arm_bare_bsp',
'TBR/Delete/BSPQuickInfo',
'TBR/Delete/BSP_Template',
'TBR/Delete/Build_Results',
'TBR/Delete/Canadian_Cross_Compiler?',
'TBR/Delete/Documentation',
'TBR/Delete/DownloadRTEMS',
'TBR/Delete/DownloadingRTEMS',
'TBR/Delete/ExecutiveVsKernelVsOperatingSystemVsRTOS',
'TBR/Delete/Fault_injection?',
'TBR/Delete/FreeBSD_Ports',
'TBR/Delete/GCCAVRBugs',
'TBR/Delete/Hierarchy',
'TBR/Delete/HowTo:_Mongoose_Web_Server',
'TBR/Delete/IDL_COM?',
'TBR/Delete/Installing_MinGW_RTEMS_Tools',
'TBR/Delete/Installing_an_Infobox',
'TBR/Delete/Libbsd-port?',
'TBR/Delete/MacOSHostedTools?',
'TBR/Delete/MacOS_Tools_From_Source',
'TBR/Delete/Makefile',
'TBR/Delete/Makefile.am',
'TBR/Delete/MinGW_Tools_for_Windows2',
'TBR/Delete/MoreBSPsForSimulators?',
'TBR/Delete/NewlibMemoryAllocation',
'TBR/Delete/OutsideSOC_64bit_timestamps',
'TBR/Delete/POSIXTimingTests?',
'TBR/Delete/RTEMSLicense',
'TBR/Delete/RTEMS_Build_Farm',
'TBR/Delete/RTEMS_CENTRE',
'TBR/Delete/RTEMS_CVS_Repository',
'TBR/Delete/RTEMS_CVS_Repository_Writing',
'TBR/Delete/RTEMS_Graphics_Toolkit',
'TBR/Delete/RecentChanges',
'TBR/Delete/SPARCengine_1e',
'TBR/Delete/SandBox',
'TBR/Delete/SpecBuilder',
'TBR/Delete/TNC',
'TBR/Delete/Tools_Used_by_the_RTEMS_Project',
'TBR/Delete/UseHashOrMapInNotepadsAndKeys',
'TBR/Delete/Virtual_Machines_for_RTEMS_Development'
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
    mentors = "\"" + str(get_mentor(b)) + "\""
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
