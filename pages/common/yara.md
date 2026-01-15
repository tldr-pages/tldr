# yara

> Pattern matching tool for identifying and classifying malware.
> See also: `yarac`.
> More information: <https://yara.readthedocs.io/en/stable/commandline.html>.

- Scan a specific file with a rule file:

`yara {{path/to/rule.yar}} {{path/to/file}}`

- Recursively scan a directory and subdirectories containing possible threats:

`yara {{path/to/rule.yar}} {{[-r|--recursive]}} {{path/to/directory}}`

- Scan a running process by its PID using multiple rules:

`yara {{path/to/rule1.yar path/to/rule2.yar ...}} {{PID}}`

- Print metadata associated with the matching rules:

`yara {{[-m|--print-meta]}} {{path/to/rule.yar}} {{path/to/file}}`

- Print the strings that caused the rule to match:

`yara {{[-s|--print-strings]}} {{path/to/rule.yar}} {{path/to/file}}`

- Use a specific number of threads for parallel scanning:

`yara {{[-p|--threads]}} {{number_of_threads}} {{path/to/rule.yar}} {{path/to/directory}}`

- Use compiled YARA rules file to scan a directory recursively:

`yara {{[-C|--compiled-rules]}} {{path/to/rules.bin}} {{[-r|--recursive]}} {{path/to/directory}}`
