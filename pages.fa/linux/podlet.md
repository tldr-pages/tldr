# podlet

> تولید فایل‌های Quadlet مربوط به Podman از دستور Podman، فایل compose یا شیء موجود.
> همچنین ببینید: `podman`.
> اطلاعات بیشتر: <https://github.com/containers/podlet>.

- تولید Quadlet معادل برای دستور podman:

`podlet {{podman_command}}`

- تولید Quadlet با نام و توضیح دلخواه:

`podlet {{[-n|--name]}} {{name}} {{[-d|--description]}} {{description}} {{podman_command}}`

- افزودن اعلان‌های وابستگی و ترتیب راه‌اندازی به Quadlet تولیدشده:

`podlet {{[-i|--install]}} --wanted-by {{unit}} --after {{unit}} {{podman_command}}`

- تولید Quadletها از فایل compose در دایرکتوری فعلی:

`podlet compose`

- تولید Quadletها برای فایل compose در دایرکتوری واحد کاربر فعلی:

`podlet {{[-u|--unit-directory]}} compose {{path/to/compose.yaml}}`
