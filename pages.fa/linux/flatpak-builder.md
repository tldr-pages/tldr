# flatpak-builder

> کمک به ساخت وابستگی‌های برنامه.
> اطلاعات بیشتر: <https://docs.flatpak.org/en/latest/flatpak-builder-command-reference.html>.

- ساخت یک Flatpak و صادر کردن آن به مخزن جدید:

`flatpak-builder {{path/to/build_directory}} {{path/to/manifest}}`

- ساخت یک Flatpak و صادر کردن آن به مخزن مشخص:

`flatpak-builder --repo {{repository_name}} {{path/to/build_directory}} {{path/to/manifest}}`

- ساخت یک Flatpak و نصب محلی آن:

`flatpak-builder --install {{path/to/build_directory}} {{path/to/manifest}}`

- ساخت و امضای یک Flatpak و صادر کردن آن به مخزن مشخص:

`flatpak-builder --gpg-sign {{key_id}} --repo {{repository_name}} {{path/to/manifest}}`

- اجرای یک پوسته در محیط ایزولهٔ برنامه بدون نصب آن:

`flatpak-builder --run {{path/to/build_directory}} {{path/to/manifest}} {{sh}}`
