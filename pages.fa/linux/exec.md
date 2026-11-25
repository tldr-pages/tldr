# exec

> اجرای یک دستور بدون ایجاد فرایند فرزند.
> اطلاعات بیشتر: <https://www.gnu.org/software/bash/manual/bash.html#index-exec>.

- اجرای یک دستور مشخص:

`exec {{command -with -flags}}`

- اجرای یک دستور با محیطی تقریباً خالی:

`exec -c {{command -with -flags}}`

- اجرای یک دستور به‌عنوان پوستهٔ ورود:

`exec -l {{command -with -flags}}`

- اجرای یک دستور با نامی متفاوت:

`exec -a {{name}} {{command -with -flags}}`
