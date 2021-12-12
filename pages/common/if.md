# if

> Performs conditional processing in shell scripts.
> See also: `test`, `[`.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs>.

- Execute the specified commands if the condition command's exit status is zero:

`if {{condition_command}}; then {{echo "Condition is true"}}; fi`

- Execute the specified commands if the condition command's exit status is not zero:

`if ! {{condition_command}}; then {{echo "Condition is true"}}; fi`

- Execute the first specified commands if the condition command's exit status is zero otherwise execute the second specified commands:

`if {{condition_command}}; then {{echo "Condition is true"}}; else {{echo "Condition is false"}}; fi`

- Check whether a [f]ile exists:

`if [[ -f {{path/to/file}} ]]; then {{echo "Condition is true"}}; fi`

- Check whether a [d]irectory exists:

`if [[ -d {{path/to/directory}} ]]; then {{echo "Condition is true"}}; fi`

- Check whether a file or directory [e]xists:

`if [[ -e {{path/to/file_or_directory}} ]]; then {{echo "Condition is true"}}; fi`

- Check whether a variable is defined:

`if [[ -n "${{variable}}" ]]; then {{echo "Condition is true"}}; fi`

- List all possible conditions (`test` is an alias to `[`; both are commonly used with `if`):

`man [`
