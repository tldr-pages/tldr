# createrepo

> Initializes an RPM repository in the given directory, including all XML and SQLite.
> More information: <https://linux.die.net/man/8/createrepo>.

- Initialize basic repository in a directory

`createrepo /path/to/directory`

- Initialize a repository, excluding test RPMs, while being verbose

`createrepo -v -x test_*.rpm /path/to/directory`

- Initialize a repository, using sha1 as the checksum algorithm, and ignoring symlinks

`createrepo -S -s sha1 /path/to/directory`
