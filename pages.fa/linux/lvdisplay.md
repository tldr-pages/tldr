# lvdisplay

> نمایش اطلاعات حجم‌های منطقی مدیر حجم منطقی (LVM).
> همچنین : `lvm`, `lvs`.
> اطلاعات بیشتر: <https://manned.org/lvdisplay>.

- نمایش اطلاعات همهٔ حجم‌های منطقی:

`sudo lvdisplay`

- نمایش اطلاعات در قالب کوتاه (مانند اجرای `lvs`):

`sudo lvdisplay {{[-C|--columns]}}`

- نمایش اطلاعات همهٔ حجم‌های منطقی در گروه حجم vg1:

`sudo lvdisplay {{vg1}}`

- نمایش اطلاعات حجم منطقی lv1 در گروه حجم vg1:

`sudo lvdisplay {{vg1/lv1}}`
