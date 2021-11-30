# if

> Performs conditional processing in shell scripts.
> See also: `test`, `[`.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs>.

- Execute the specified commands if the condition command's exit status is zero:

`if {{condition_command}}; then {{commands}}; fi`

- Execute the specified commands if the condition command exit status is nonzero:

`if ! {{condition_command}}; then {{commands}}; fi`

- Execute the first specified commands if the condition command exit status is zero otherwise execute the second specified commands:

`if {{condition_command}}; then {{first_commands}}; else {{second_commands}}; fi`

- Check whether a file exists:

`if [[ -f "{{path/to/file}}" ]]; then {{commands}}; fi`

- Check whether a directory exists:

`if [[ -d "{{path/to/directory}}" ]]; then {{commands}}; fi`

- Check whether a file or directory exists:

`if [[ -e "{{path/to/file_or_directory}}" ]]; then {{commands}}; fi`

- Check whether a variable is defined:

`if [[ -n "{{$VARIABLE}}" ]]; then {{commands}}; fi`

- List all possible conditions (`test` is an alias to `[`; both are commonly used with `if`):

`man [`
