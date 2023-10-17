# Base 64

> बेस 64 प्रस्तुतीकरण का उपयोग करके कोड और डिकोड करें।
> अधिक जानकारी: <https://www.unix.com/man-page/osx/1/base64/>।

- फ़ाइल को कोड करें:

`base64 --input={{plain_file}}`

- फ़ाइल को डिकोड करें:

`base64 --decode --input={{base64_file}}`

- `stdin` से कोड करें:

`echo -n "{{plain_text}}" | base64`

- `stdin` से डिकोड करें:

`echo -n {{base64_text}} | base64 --decode`
