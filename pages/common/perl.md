# perl

> The Perl 5 language interpreter.
> More information: <https://www.perl.org>.

- Print lines from `stdin` [m/] matching regex1 and case insensitive [/i] regex2:

`perl -n -e 'print if m/{{regex1}}/ and m/{{regex2}}/i'`

- Say [-E] first match group, using a regexp, ignoring space in regex [/x]:

`perl -n -E 'say $1 if m/{{before}} (  {{group_regex}}  ) {{after}}/x'`

- [-i]n-place, with backup, [s/] substitute all occurrence [/g] of regex with replacement:

`perl -i'.bak' -p -e 's/{{regex}}/{{replacement}}/g' {{path/to/files}}`

- Use perl's inline documentation, some pages also available via manual pages on Linux:

`perldoc perlrun ; perldoc module ; perldoc -f splice; perldoc -q perlfaq1`
