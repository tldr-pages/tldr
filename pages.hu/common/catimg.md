# catimg

> Képnyomtatás a terminálban Lásd még: `pixterm`, `chafa`. További információ: [https://github.com/posva/catimg.](https://github.com/posva/catimg)

- JPEG, PNG vagy GIF kép nyomtatása a terminálra:

`catimg {{path/to/file}}`

- Duplázza meg a kép \[r\]felbontását:

`catimg -r 2 {{path/to/file}}`

- A 24 bites szín kikapcsolása a jobb \[t\]erminális támogatás érdekében:

`catimg -t {{path/to/file}}`

- Egyéni \[w\]idth vagy \[H\]nyolc megadása:

`catimg {{-w|-H}} {{40}} {{path/to/file}}`
