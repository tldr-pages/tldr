# wiggle

> A patch application tool resolving conflicts in patches that `patch` cannot handle.
> Note: Wiggle forcefully applies all changes, merging when conflicts arise, and reporting unresolvable issues.
> More information: <https://manned.org/wiggle>.

- Apply changes from the patch file to the original file:

`wiggle {{path/to/file.patch}}`

- Apply changes to the output file:

`wiggle {{path/to/file.patch}} {{[-o|--output]}} {{path/to/output_file.txt}}`

- Take any changes in `file.rej` that could not have been applied and merge them into a file:

`wiggle {{[-r|--replace]}} {{path/to/file}} {{path/to/file.rej}}`

- Extract one branch of a patch or merge file:

`wiggle {{[-x|--extract]}} {{path/to/file.patch}}`

- Apply a patch and save the compared words to the output file:

`wiggle {{[-w|--words]}} {{path/to/my_word_patch.patch}} {{[-o|--output]}} {{path/to/word_patched_code.c}}`

- Display help about the merge function:

`wiggle {{[-m|--merge]}} {{[-h|--help]}}`
