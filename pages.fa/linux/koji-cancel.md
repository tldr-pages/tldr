# koji cancel

> لغو کارهای فعال در سیستم ساخت Koji.
> اطلاعات بیشتر: <https://docs.pagure.org/koji/>.

- لغو یک کار با شناسهٔ آن:

`koji cancel {{task_id}}`

- لغو چند کار:

`koji cancel {{task_id1 task_id2 ...}}`

- لغو یک کار با خروجی مفصل:

`koji cancel --verbose {{task_id}}`

- نمایش راهنما:

`koji cancel {{[-h|--help]}}`
