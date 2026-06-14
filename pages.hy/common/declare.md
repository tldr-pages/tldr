#հայտարարել

> Հայտարարել փոփոխականները և տալ նրանց ատրիբուտներ:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#index-declare>:.

- Հայտարարեք տողային փոփոխական՝ նշված արժեքով.:

`declare {{variable}}="{{value}}"`

- Հայտարարեք ամբողջ թվով փոփոխական՝ նշված արժեքով.:

`declare -i {{variable}}="{{value}}"`

- Հայտարարեք զանգվածի փոփոխական՝ նշված արժեքով.:

`declare -a {{variable}}=({{item_a item_b item_c}})`

- Հայտարարեք ասոցիատիվ զանգվածի փոփոխական՝ նշված արժեքով.:

`declare -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- Հայտարարեք միայն կարդալու տողային փոփոխական՝ նշված արժեքով.:

`declare -r {{variable}}="{{value}}"`

- Նշված արժեքով ֆունկցիայի ներսում գլոբալ փոփոխական հայտարարեք.:

`declare -g {{variable}}="{{value}}"`

- Տպել ֆունկցիայի սահմանումը.:

`declare -f {{function_name}}`

- Տպել փոփոխականի սահմանումը.:

`declare -p {{variable_name}}`
