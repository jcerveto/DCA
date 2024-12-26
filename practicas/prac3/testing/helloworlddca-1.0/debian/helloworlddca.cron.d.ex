#
# Regular cron jobs for the helloworlddca package.
#
0 4	* * *	root	[ -x /usr/bin/helloworlddca_maintenance ] && /usr/bin/helloworlddca_maintenance
