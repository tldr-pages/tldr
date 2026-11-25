# nft monitor

> نمایش تغییرات بلادرنگ در دیوار آتش لینوکس `nftables`.
> اطلاعات بیشتر: <https://manned.org/nft#head21>.

- پایش همهٔ رویدادهای nftables:

`sudo nft monitor`

- پایش فقط به‌روزرسانی قوانین (افزودن، حذف، جایگزینی):

`sudo nft monitor rules`

- پایش به‌روزرسانی مجموعه و عناصر:

`sudo nft monitor sets`

- پایش رویدادها و چاپ خروجی JSON:

`sudo nft {{[-j|--json]}} monitor`
