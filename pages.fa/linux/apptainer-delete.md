# apptainer delete

> حذف تصاویر کانتینر از یک کتابخانهٔ راه دور.
> اطلاعات بیشتر: <https://apptainer.org/docs/user/main/cli/apptainer_delete.html>.

- حذف یک تصویر از کتابخانهٔ کانتینر:

`apptainer delete library://{{user/collection/container}}:{{tag}}`

- حذف یک تصویر برای یک معماری مشخص:

`apptainer delete {{[-A|--arch]}} {{amd64|arm64|ppc64le}} library://{{user/collection/container}}:{{tag}}`

- حذف اجباری یک تصویر بدون درخواست تأیید:

`apptainer delete {{[-F|--force]}} library://{{user/collection/container}}:{{tag}}`

- حذف یک تصویر از یک سرور کتابخانهٔ مشخص:

`apptainer delete --library {{https://library.example.com}} library://{{user/collection/container}}:{{tag}}`

- حذف یک تصویر با استفاده از HTTP به جای HTTPS:

`apptainer delete --no-https library://{{hostname/user/collection/container}}:{{tag}}`

- نمایش راهنما:

`apptainer delete {{[-h|--help]}}`
