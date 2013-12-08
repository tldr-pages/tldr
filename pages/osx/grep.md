# grep

- Matches patterns in input text
- Supports simple patterns and regular expressions

## Search for an exact string
`grep something FILE`

## Use a regex instead of a word

`grep -e ^regex$ FILE`

## See 3 lines of context

`grep -C 3 something FILE`

## Print the count of matches

`grep -c something FILE`

## Use the standard input instead

`cat FILE | grep something`
