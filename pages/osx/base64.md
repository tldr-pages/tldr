# base64

> Encode and decode using Base64 representation.

- Encode a file:

`base64 --input={{plain_file}}`

- Decode a file:

`base64 --decode --input={{base64_file}}`

- Encode from stdin:

`echo -n {{plain_text}} | base64`

- Decode from stdin:

`echo -n {{base64_text}} | base64 --decode`
