#!/bin/bash
# Pre-remove script

# Condition: Check if /tmp directory exists (which it always should)
if [ -d /tmp ]; then
    echo "/tmp directory exists. Proceeding with removal."
    echo "REMOVAL SUCCESSFUL!" > /tmp/aaa_remove_congrats.txt
else
    echo "/tmp directory does not exist. Exiting."
    exit 1
fi

# Continue with the rest of the pre-install script
echo "Pre-install checks passed!"
