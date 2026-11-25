# dconf write

> نوشتن مقادیر کلیدها در پایگاه‌های دادهٔ dconf.
> اطلاعات بیشتر: <https://manned.org/dconf>.

- نوشتن مقدار یک کلید مشخص:

`dconf write /{{path/to/key}} "{{value}}"`

- نوشتن مقدار رشته‌ای یک کلید مشخص:

`dconf write /{{path/to/key}} "'{{string}}'"`

- نوشتن مقدار صحیح یک کلید مشخص:

`dconf write /{{path/to/key}} "{{5}}"`

- نوشتن مقدار بولی یک کلید مشخص:

`dconf write /{{path/to/key}} "{{true|false}}"`

- نوشتن مقدار آرایه‌ای یک کلید مشخص:

`dconf write /{{path/to/key}} "[{{'first', 'second', ...}}]"`

- نوشتن یک آرایهٔ خالی به‌عنوان مقدار کلید مشخص:

`dconf write /{{path/to/key}} "@as []"`
