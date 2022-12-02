# base64

> Encode and decode using Base64 representation.
> More information: <https://www.unix.com/man-page/osx/1/base64/>.

- Encode a file:

`base64 --input={{path/to/file}}`

- Decode a file:

`base64 --decode --input={{path/to/file}}`

- Encode from `stdin`:

`echo -n "{{plain_text}}" | base64`

- Decode from `stdin`:

`echo -n {{base64_text}} | base64 --decode`
