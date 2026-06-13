# comby

> Tool for structural code search and replace that supports many languages.
> More information: <https://github.com/comby-tools/comby>.

- Match and rewrite templates, and print changes:

`comby '{{assert_eq!(:[a], :[b])}}' '{{assert_eq!(:[b], :[a])}}' {{.rs}}`

- Match and rewrite with rewrite properties:

`comby '{{assert_eq!(:[a], :[b])}}' '{{assert_eq!(:[b].Capitalize, :[a])}}' {{.rs}}`

- Match and rewrite in-place:

`comby -in-place '{{match_pattern}}' '{{rewrite_pattern}}'`

- Only perform matching and print matches:

`comby -match-only '{{match_pattern}}' ""`
