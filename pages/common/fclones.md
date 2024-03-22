# fclones

> Efficient duplicate file finder and remover.
> More information: <https://github.com/pkolaczk/fclones>.

- Search a current directory:

`fclones group .`

- Search multiple directories and cache results:

`fclones group --cache {{directory1}} {{directory2}}`

- Search only the specified directory skipping the subdirectory and save the results into a file:

`fclones group {{path/to/directory}} --depth 1 > dupes.txt`

- Move the duplicates  in a `dupes.txt` to a different directory:

`fclones move {{path/to/target_directory}} <dupes.txt`

- Perform a dry run for soft links  in a `dupes.txt` file without actually linking:

`fclones link --soft <dupes.txt --dry-run 2>/dev/null`

- Delete the newest duplicates from the current directory without storing them in a file:

`fclones group . | fclones remove --priority newest`

- Preprocess jpg files in the current directory by using an external command  to strip their exif data before matching for duplicates:

`fclones group . --name '*.jpg' -i --transform 'exiv2 -d a $IN' --in-place`