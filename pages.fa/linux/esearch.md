# esearch

> انجام جست‌وجوی جدید Entrez با استفاده از عبارت‌ها در فیلدهای نمایه‌شده.
> بخشی از بستهٔ `edirect` است.
> اطلاعات بیشتر: <https://www.ncbi.nlm.nih.gov/books/NBK179288/>.

- جست‌وجوی مهارکنندهٔ انتخابی بازجذب سروتونین در پایگاه دادهٔ pubmed:

`esearch -db pubmed -query "{{selective serotonin reuptake inhibitor}}"`

- جست‌وجوی پایگاه دادهٔ پروتئین با پرس‌وجو و عبارت منظم `regex`:

`esearch -db {{protein}} -query '{{Escherichia*}}'`

- جست‌وجوی توالی‌هایی در پایگاه دادهٔ نوکلئوتیدی که فرادادهٔ آن‌ها حاوی انسولین و جوندگان است:

`esearch -db nuccore -query "{{insulin [PROT] AND rodents [ORGN]}}"`

- نمایش راهنما:

`esearch {{[-h|-help]}}`
