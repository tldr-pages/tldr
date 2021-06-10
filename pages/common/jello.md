# jello

> A command-line JSON processor using python syntax.
> More information: <https://github.com/kellyjonbrazil/jello>.

- Output JSON or JSON Lines STDIN data, in pretty-print format:

`cat {{file.json}} | jello`

- Output a grepable schema from JSON or JSON Lines STDIN data:

`cat {{file.json}} | jello -s`

- Output all elements from arrays (or all the values from objects) in JSON or JSON Lines STDIN data:

`cat {{file.json}} | jello -l`

- Output the first element in JSON or JSON Lines STDIN data:

`cat {{file.json}} | jello _[0]`

- Output the value of a given key of each element in JSON or JSON Lines STDIN data:

`cat {{file.json}} | jello '[i.{{key_name}} for i in _]'`

- Output the value of multiple keys as a new JSON object (assuming the input JSON has the keys `key_name` and `other_key_name`):

`cat {{file.json}} | jello '{{{"my_new_key"}}: _.{{key_name}}, {{"my_other_key"}}: _.{{other_key_name}}}'`

- Output raw string lines or JSON lines using a loop. (Useful for assigning to a BASH variable or array):

```
cat {{file.json}} | jello -lr '\
result = []
for i in _:
    if i == "foo":
        result.append(i)
result'
```
