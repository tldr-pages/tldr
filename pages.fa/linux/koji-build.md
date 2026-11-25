# koji build

> ساخت بستهٔ RPM.
> اطلاعات بیشتر: <https://docs.pagure.org/koji/>.

- ساخت بسته از `src.rpm`:

`koji build {{target}} {{path/to/src.rpm}}`

- ساخت بسته از URL سیستم مدیریت کد منبع (SCM):

`koji build {{target}} {{git+https://src.fedoraproject.org/rpms/vim.git#e847a50297a216229050bf4db3d06a139104e7cf}}`

- انجام ساخت آزمایشی (scratch):

`koji build {{target}} {{path/to/src.rpm}} --scratch`

- انتظار برای ساخت، حتی اگر در پس‌زمینه اجرا شود:

`koji build {{target}} {{path/to/src.rpm}} --wait`

- منتظر نماندن برای ساخت:

`koji build {{target}} {{path/to/src.rpm}} --nowait`

- نمایش راهنما:

`koji build {{[-h|--help]}}`
