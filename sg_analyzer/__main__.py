#!/usr/bin/python
import sys

from security.security_groups import Security

helping = """
AWS Analyzer SG.

Usage:
  main.py --analyze (Analyzes all ec2 running and all security groups)
  main.py --compromised (Analyzes all SG with rules to 0.0.0.0/0)
    --port (If you want to analyze a specific port)
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

def main():
    #Passar vazio caso esteja no profile
    sec_obj = Security("", "", "")
    if "--help" in sys.argv:
        print helping
    elif "--analyze" in sys.argv:
        #analyze security groups of ec2 instances
        sec_obj.get_security_groups_all_instances()
    elif "--compromised" in sys.argv:
        port = ""
        if "--port" in sys.argv:
            port = sys.argv[3]
        sec_obj.get_sg_compromised(port)
    else:
        print "Not found :("
        print helping


if __name__== "__main__":
  main()