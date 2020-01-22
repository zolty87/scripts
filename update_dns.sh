#!/bin/bash
# Add this to .bash_profile:
## SSH_COMPLETE=`cat ~/.dns_completion`
## complete -o default -W "${SSH_COMPLETE[*]}" ping ssh telnet host mtr

dns_file=~/.dns_completion

(host -l net.uw.edu.pl ns3.uw.edu.pl && host -l rtr.net.uw.edu.pl ns3.uw.edu.pl && (cat ~/.ssh/known_hosts | cut -f 1 -d " "|tr -s "," "\n"|sort|uniq) )| grep -v "name server" | awk '{print$1}' | sort | uniq | grep -v "Address:\|Aliases:\|Name:\|Using" > $dns_file
