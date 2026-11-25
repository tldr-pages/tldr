# bsub

> ارسال کارهای دسته‌ای به زمان‌بند LSF (Load Sharing Facility).
> اطلاعات بیشتر: <https://www.ibm.com/docs/spectrum-lsf/latest?topic=reference-bsub>.

- ارسال یک فایل اسکریپت به‌عنوان کار:

`bsub {{path/to/script.sh}}`

- ارسال یک کار به صف مشخص:

`bsub -q {{queue_name}} make all`

- ارسال یک کار با نام و هدایت خروجی و خطا:

`bsub -J {{job_name}} --output {{path/to/output.log}} --error {{path/to/error.log}} {{path/to/script.sh}}`

- درخواست ۸ هستهٔ پردازنده و ۱۶ گیگابایت حافظه برای یک دستور:

`bsub -n 8 -M 16G cargo build --release`

- اجرای یک پوستهٔ تعاملی در نشست فعلی:

`bsub -I bash`

- ارسال یک کار با محدودیت زمان اجرای ۴۵ دقیقه:

`bsub -W 45 {{path/to/script.sh}}`
