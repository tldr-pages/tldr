# cliphist

> مدیریت تاریخچهٔ کلیپ‌بورد برای ترکیب‌گرهای Wayland.
> با `wl-copy` و `wl-paste` کار می‌کند.
> اطلاعات بیشتر: <https://github.com/sentriz/cliphist#usage>.

- فهرست کردن موارد تاریخچهٔ کلیپ‌بورد:

`cliphist list`

- انتخاب و کپی کردن یک مورد قبلی کلیپ‌بورد با استفاده از `fzf`:

`cliphist list | fzf | cliphist decode | wl-copy`

- حذف همهٔ موارد ذخیره‌شدهٔ کلیپ‌بورد:

`cliphist wipe`

- حذف یک مورد مشخص کلیپ‌بورد با شناسه:

`echo {{entry_id}} | cliphist delete`

- ذخیرهٔ دستی محتوای فعلی کلیپ‌بورد:

`wl-paste | cliphist store`
