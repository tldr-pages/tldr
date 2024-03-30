# boxes

> کشیدن، حذف و تعمیر جعبه های هنری اسکی.
> اطلاعات بیشتر: <https://boxes.thomasjensen.com/boxes-man-1.html>.

- کشیدن یک جعبه در اطراف یک رشته:

`echo "{{string}}" | boxes`

- حذف جعبه از یک رشته:

`echo "{{string}}" | boxes -r`

- کشیدن یک جعبه با طرح دلخواه در اطراف یک رشته:

`echo "{{string}}" | boxes -d {{parchment}}`

- کشیدن یک جعبه به طول 10 و ارتفاع 5:

`echo "{{string}}" | boxes -s {{10}}x{{5}}`

- کشیدن یک جعبه با متن در وسط:

`echo "{{string}}" | boxes -a c`
