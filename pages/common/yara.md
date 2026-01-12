# yara

> Pattern matching tool for identifying and classifying malware.
> See also: `yarac`.
> More information: <https://yara.readthedocs.io/en/stable/commandline.html>.

- Scan a specific file with a rule file:

`yara {{path/to/rules.yar}} {{path/to/target_file}}`

- Recursively scan a directory containing possible threats:

`yara {{path/to/rules.yar}} {{[-r|--recursive]}} {{path/to/directory}}`

- Scan a running process by its PID using multiple rules:

`yara {{path/to/rules1.yar path/to/rules2.yar ...}} {{pid}}`

- Only print rules that match (negate results with `--negate` to show non-matches):

`yara {{[-w|--no-warnings]}} {{path/to/rules.yar}} {{path/to/target}}`

- Print metadata associated with the matching rules:

`yara {{[-m|--print-meta]}} {{path/to/rules.yar}} {{path/to/target}}`

- Print the strings that caused the rule to match:

`yara {{[-s|--print-strings]}} {{path/to/rules.yar}} {{path/to/target}}`

- Use a specific number of threads for parallel scanning with the rules in a directory:

`yara {{[-p|--threads]}} {{number_of_threads}} {{path/to/rules.yar}} {{path/to/target}}`


