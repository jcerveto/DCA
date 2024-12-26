#!/bin/bash
# Pre-install script

# Condition: Check if /tmp directory exists (which it always should)
if [ -d /tmp ]; then
    echo "/tmp directory exists. Proceeding with installation."
    echo "INSTALLATION SUCCESSFUL!" > /tmp/aaa_install_congrats.txt
else
    echo "/tmp directory does not exist. Exiting."
    exit 1
fi

# Continue with the rest of the pre-install script
echo "Pre-install checks passed!"
