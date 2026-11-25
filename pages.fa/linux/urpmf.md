# urpmf

> یافتن فایل‌ها در بسته‌ها و پرس‌وجوی اطلاعات آن‌ها در Mageia.
> همچنین ببینید: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmi.update`, `urpmq`.
> اطلاعات بیشتر: <https://man.linuxreviews.org/man8/urpmf.8.html>.

- جست‌وجوی بسته‌های حاوی فایل:

`urpmf {{filename}}`

- جست‌وجوی بسته‌هایی که در خلاصهٔ آن‌ها یک کلیدواژه و کلیدواژهٔ دیگر وجود دارد:

`urpmf --summary {{keyword1}} -a {{keyword2}}`

- جست‌وجوی بسته‌هایی که در توضیحات آن‌ها یک کلیدواژه یا کلیدواژهٔ دیگر وجود دارد:

`urpmf --description {{keyword1}} -o {{keyword2}}`

- جست‌وجوی بسته‌هایی که نامشان حاوی کلیدواژه نیست، بدون حساسیت به بزرگی حروف و با استفاده از «|» به‌عنوان جداکنندهٔ فیلد (پیش‌فرض «:»):

`urpmf --description ! {{keyword}} -F'|'`
