# nixos-option

> بررسی پیکربندی NixOS.
> اطلاعات بیشتر: <https://nixos.org/manual/nixos/stable/index.html#sec-modularity>.

- فهرست کردن همهٔ زیرکلیدهای کلید گزینهٔ مشخص:

`nixos-option {{option_key}}`

- فهرست کردن ماژول‌های هستهٔ راه‌اندازی فعلی:

`nixos-option boot.kernelModules`

- فهرست کردن کلیدهای مجاز کاربر مشخص:

`nixos-option users.users.{{username}}.openssh.authorizedKeys.{{keyFiles|keys}}`

- فهرست کردن همهٔ سازنده‌های راه دور:

`nixos-option nix.buildMachines`

- فهرست کردن همهٔ زیرکلیدهای کلید مشخص در پیکربندی دیگر NixOS:

`NIXOS_CONFIG={{path/to/configuration.nix}} nixos-option {{option_key}}`

- نمایش بازگشتی همهٔ مقادیر یک کاربر:

`nixos-option {{[-r|--recursive]}} users.users.{{user}}`
