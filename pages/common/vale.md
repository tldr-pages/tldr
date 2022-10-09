# vale

> Extensible style checker that supports multiple markup formats, such as Markdown and AsciiDoc.
> More information: <https://vale.sh/>.

- Check the style of a file:

`vale {{file}}`

- Check the style of a file with a specified configuration:

`vale --config='{{path/to/.vale.ini}}' {{file}}`

- Output the results in JSON format:

`vale --output=JSON {{file}}`

- Only list issues at or above the specified severity:

`vale --minAlertLeve={{suggestion|warning|error}} {{file}}`

- Check the style from STDIN, specifying markup format:

`cat {{file.md}} | vale --ext=.md`

- List the current configuration:

`vale ls-config`
