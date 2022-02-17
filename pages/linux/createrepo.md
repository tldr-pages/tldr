# createrepo

> Initializes an RPM repository in the given directory, including all XML and SQLite files.
> More information: <https://manned.org/createrepo>.

- Initialize a basic repository in a directory:

`createrepo /path/to/directory`

- Initialize a repository, exclude test RPMs and display verbose logs:

`createrepo -v -x test_*.rpm /path/to/directory`

- Initialize a repository, use sha1 as the checksum algorithm, and ignore symlinks:

`createrepo -S -s sha1 /path/to/directory`
