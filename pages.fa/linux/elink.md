# elink

> جست‌وجوی همسایه‌های ازپیش‌محاسبه‌شده در یک پایگاه داده یا یافتن رکوردهای مرتبط در پایگاه‌های دادهٔ دیگر.
> بخشی از بستهٔ `edirect` است.
> اطلاعات بیشتر: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- جست‌وجو در pubmed و سپس یافتن توالی‌های مرتبط:

`esearch -db pubmed -query "{{selective serotonin reuptake inhibitor}}" | elink -target nuccore`

- جست‌وجو در پایگاه نوکلئوتیدی و سپس یافتن نمونه‌های زیستی مرتبط:

`esearch -db nuccore -query "{{insulin [PROT] AND rodents [ORGN]}}" | elink -target biosample`
