# rpmconf

> Handle RPMNEW, RPMSAVE and RPMORIG files left over by package upgrades.
> More information: <https://docs.fedoraproject.org/en-US/quick-docs/upgrading-fedora-offline/#sect-optional-post-upgrade-tasks>.

- Search for all leftover files and interactively choose what to do with each of them:

`sudo rpmconf -a`

- Delete orphaned RPMNEW or RPMSAVE files:

`sudo rpmconf -ac`
