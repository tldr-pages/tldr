# cb

> بریدن، رونوشت و چسباندن هرچیزی در ترمینال.
> اطلاعات بیشتر: <https://github.com/Slackadays/Clipboard>.

- نمایش تمام کلیپ بوردها:

`cb`

- رونوشت یک فایل به کلیپ بورد:

`cb copy {{path/to/file}}`

- کپی متن دلخواه به کلیپ بورد:

`cb copy "{{Some example text}}"`

- رونوشت داده ی هدایت شده به داخل در کلیپ بورد:

`echo "{{Some example text}}" | cb`

- چسباندن محتوای کلیپ بورد:

`cb paste`

- هدایت محتوای کلیپ بورد به خارج:

`cb | cat`

- نمایش تاریخچه کلیپ بورد:

`cb history`

- نمایش اطلاعات کلیپ بورد:

`cb info`
