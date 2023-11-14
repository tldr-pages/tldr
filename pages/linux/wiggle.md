# wiggle

> A patch application tool resolving conflicts in patches that `patch` cannot handle.
> Note: Wiggle forcefully applies all changes, merging when conflicts arise, and reporting unresolvable issues.
> More information: <https://www.unix.com/man-page/suse/1/wiggle/>.

- Apply changes from the patch file to the original file:

`wiggle {{path/to/my_patch.patch}}`

- Apply changes to the [o]utput file:

`wiggle {{path/to/my_patch.patch}} -o {{path/to/output_file.txt}}`

- Take any changes in `file.rej` that could not have been applied and merge them into a file:

`wiggle --replace {{path/to/file}} {{path/to/file.rej}}`

- E[x]tract one branch of a patch or merge file:

`wiggle -x {{path/to/my_patch.patch}}`

- Apply patch and the compared [words] are saved to an [o]utput file:

`wiggle --words {{path/to/my_word_patch.patch}} -o {{path/to/word_patched_code.c}}`

- Get [help] about the [merge] function of wiggle:

`wiggle --merge --help`
