# settings

> Menampilkan informasi terhadap pengaturan sistem operasi Android.
> Informasi lebih lanjut: <https://adbinstaller.com/commands/adb-shell-settings-5b670d5ee7958178a2955536>.

- Menampilkan daftar pengaturan di dalam namespace `global`:

`settings list {{global}}`

- Menampilkan nilai dari pengaturan tertentu:

`settings get {{global}} {{airplane_mode_on}}`

- Menyetel nilai pengaturan tertentu:

`settings put {{system}} {{screen_brightness}} {{42}}`

- Menghapus nilai pengaturan tertentu:

`settings delete {{secure}} {{screensaver_enabled}}`
