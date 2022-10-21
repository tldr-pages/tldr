# settings

> Tampilkan informasi terhadap pengaturan sistem operasi Android.
> Informasi lebih lanjut: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Tampilkan daftar pengaturan di dalam namespace `global`:

`settings list {{global}}`

- Tampilkan nilai dari pengaturan tertentu:

`settings get {{global}} {{airplane_mode_on}}`

- Setel nilai pengaturan tertentu:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Hapus nilai pengaturan tertentu:

`settings delete {{secure}} {{screensaver_enabled}}`
