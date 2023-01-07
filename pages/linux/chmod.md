# chmod

> Change file/directory access permissions.
> More information: <https://www.gnu.org/software/coreutils/chmod>.

- Add [r]ead or [w]rite or e[x]ecute permissions for a file or directory owner:

`chmod u+{{r|w|x}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Add specific permissions for an owner/users in [g]roup/[o]ther users/[a]ll at once:

`chmod {{u|g|o|a}}+{{r}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Add or remove or replace specific permissions:

`chmod {{u}}{{+|-|=}}{{r}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Remove all permissions:

`chmod {{o}}= {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Change permissions [recursive]ly:

`chmod --recursive {{u}}{{+}}{{r}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`
