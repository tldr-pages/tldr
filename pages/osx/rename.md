# rename

> Rename a file or group of files with a regular expression.
> Note: This page refers to the Perl-powered file rename script.
> WARNING: This command will overwrite files without prompting unless the dry-run option is used.
> More information: <http://plasmasturm.org/code/rename/>.

- Replace `from` with `to` in the filenames of the specified files:

`rename 's/{{from}}/{{to}}/' {{*.txt}}`

- Dry-run - display which changes would occur without performing them:

`rename {{[-n|--dry-run]}} 's/{{from}}/{{to}}/' {{*.txt}}`

- Change the extension:

`rename 's/\.old$/\.new/' {{*.txt}}`

- Change to lowercase:

`rename {{[f|--force]}} 'y/A-Z/a-z/' {{*.txt}}`

- Capitalize first letter of every word in the name:

`rename {{[f|--force]}} 's/\b(\w)/\U$1/g' {{*.txt}}`

- Replace spaces with underscores:

`rename 's/\s+/_/g' {{*.txt}}`
