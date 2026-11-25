# koji download-build

> بارگیری بستهٔ ساخته‌شده.
> اطلاعات بیشتر: <https://docs.pagure.org/koji/>.

- بارگیری همهٔ بسته‌های RPM از ساخت مشخص:

`koji download-build {{BuildID|RPM|NVR}}`

- بارگیری بسته‌های RPM امضاشده با کلید مشخص:

`koji download-build {{BuildID|RPM|NVR}} --key {{key}}`

- بارگیری فقط بسته‌های RPM برای معماری مشخص:

`koji download-build {{BuildID|RPM|NVR}} --arch {{x86_64,aarch64,noarch,...}}`

- بارگیری بستهٔ RPM مشخص:

`koji download-build {{RPM}} --rpm`

- نمایش راهنما:

`koji download-build {{[-h|--help]}}`
