# wiggle

> Wiggle is a patch application tool resolving conflicts in patches that `patch` cannot handle.
> Note: Wiggle forcefully applies all changes, merging when conflicts arise, and reporting unresolvable issues.
> More information: <https://www.unix.com/man-page/suse/1/wiggle/>.

- Apply changes from the patch file to the original file:

`wiggle {{path/to/my_patch.patch}}`

- Apply changes to an [o]utput file:

`wiggle {{path/to/my_patch.patch}} -o {{path/to/output_file.txt}}`

- Take any changes in file.rej that patch could not apply, and merge them into file:

`wiggle --replace {{path/to/file}} {{path/to/file.rej}}`

- E[x]tract one branch of patch or merge file:

`wiggle -x {{path/to/my_patch.patch}}`

- Apply patch and the compared [words] are saved to an [o]utput file:

`wiggle --words {{path/to/my_word_patch.patch}} -o {{path/to/word_patched_code.c}}`

- Get [help] about the [merge] function of wiggle:

`wiggle --merge --help`
