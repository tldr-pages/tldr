# gsettings

> پرس‌وجو و تغییر تنظیمات dconf با اعتبارسنجی طرح‌واره.
> اطلاعات بیشتر: <https://manned.org/gsettings>.

- تنظیم مقدار کلید؛ اگر کلید وجود نداشته باشد یا مقدار خارج از بازه باشد ناموفق می‌شود:

`gsettings set {{org.example.schema}} {{example_key}} {{value}}`

- چاپ مقدار کلید یا مقدار پیش‌فرض طرح‌واره اگر کلید در `dconf` تنظیم نشده باشد:

`gsettings get {{org.example.schema}} {{example_key}}`

- لغو تنظیم کلید برای استفاده از مقدار پیش‌فرض طرح‌وارهٔ آن:

`gsettings reset {{org.example.schema}} {{example_key}}`

- نمایش همهٔ طرح‌واره‌های غیرقابل‌جابه‌جایی، کلیدها و مقادیر:

`gsettings list-recursively`

- نمایش همهٔ کلیدها و مقادیر یک طرح‌واره (در صورت تنظیم نبودن، مقدار پیش‌فرض):

`gsettings list-recursively {{org.example.schema}}`

- نمایش مقادیر مجاز طرح‌واره برای کلید (مفید برای کلیدهای enum):

`gsettings range {{org.example.schema}} {{example_key}}`

- نمایش توضیح خوانای یک کلید:

`gsettings describe {{org.example.schema}} {{example_key}}`
