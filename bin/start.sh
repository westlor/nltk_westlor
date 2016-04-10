#!/bin/bash

# Conifg the env.
basepath=$(cd `dirname $0`; pwd)
echo "basepath=$basepath"
source $basepath/../env/env.conf


# Now start.
echo "Mode:0-r_shell,1-r_file,2-..."
read -p "Please select a mode:" mode


