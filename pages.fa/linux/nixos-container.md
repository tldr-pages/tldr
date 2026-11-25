# nixos-container

> شروع کانتینرهای NixOS با استفاده از کانتینرهای لینوکس.
> اطلاعات بیشتر: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- فهرست کردن کانتینرهای در حال اجرا:

`sudo nixos-container list`

- ایجاد کانتینر NixOS با فایل پیکربندی مشخص:

`sudo nixos-container create {{container_name}} --config-file {{path/to/nix_config_file}}`

- شروع، توقف، پایان اجباری یا حذف کانتینر مشخص:

`sudo nixos-container {{start|stop|terminate|destroy|status}} {{container_name}}`

- اجرای دستور در کانتینر در حال اجرا:

`sudo nixos-container run {{container_name}} -- {{command}} {{command_arguments}}`

- به‌روزرسانی پیکربندی کانتینر:

`sudo $EDITOR /var/lib/container/{{container_name}}/etc/nixos/configuration.nix && sudo nixos-container update {{container_name}}`

- ورود به نشست پوستهٔ تعاملی در کانتینری که قبلاً شروع شده است:

`sudo nixos-container root-login {{container_name}}`
