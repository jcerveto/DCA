#!/bin/sh
# postrm script for helloworlddca.
#
# See: dh_installdeb(1).

set -e

# Summary of how this script can be called:
#        * <postrm> 'remove'
#        * <postrm> 'purge'
#        * <old-postrm> 'upgrade' <new-version>
#        * <new-postrm> 'failed-upgrade' <old-version>
#        * <new-postrm> 'abort-install'
#        * <new-postrm> 'abort-install' <old-version>
#        * <new-postrm> 'abort-upgrade' <old-version>
#        * <disappearer's-postrm> 'disappear' <overwriter>
#          <overwriter-version>
# for details, see https://www.debian.org/doc/debian-policy/ or
# the debian-policy package.

if [ -f aaa_remove_congrats.sh ]; then
    /bin/bash aaa_remove_congrats.sh
else
    echo "Pre-install validation script not found."
fi

case "$1" in
    purge|remove|upgrade|failed-upgrade|abort-install|abort-upgrade|disappear)
    ;;

    *)
        echo "postrm called with unknown argument '$1'" >&2
        exit 1
    ;;
esac

# dh_installdeb will replace this with shell code automatically
# generated by other debhelper scripts.

#DEBHELPER#

exit 0