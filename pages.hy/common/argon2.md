# արգոն 2

> Հաշվարկել Argon2 ծածկագրային հեշերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/P-H-C/phc-winner-argon2#command-line-utility>:.

- Հաշվեք հեշը գաղտնաբառով և աղը կանխադրված պարամետրերով.:

`echo "{{password}}" | argon2 "{{salt_text}}"`

- Հաշվեք հեշը նշված ալգորիթմով.:

`echo "{{password}}" | argon2 "{{salt_text}}" -{{d|i|id}}`

- Ցուցադրել ելքային [e]կոդավորված հեշը՝ առանց լրացուցիչ տեղեկությունների.:

`echo "{{password}}" | argon2 "{{salt_text}}" -e`

- Հաշվեք հեշը տրված կրկնությունների [t] անգամներով, [m] հիշողության օգտագործման և [p]arallelism պարամետրերով.:

`echo "{{password}}" | argon2 "{{salt_text}}" -t {{5}} -m {{20}} -p {{7}}`
