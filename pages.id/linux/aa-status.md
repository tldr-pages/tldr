# aa-status

> Tampilkan daftar modul AppArmor yang saat ini dimuat.
> Lihat juga: `aa-complain`, `aa-disable`, `aa-enforce`.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-status.8>.

- Periksa status:

`sudo aa-status`

- Tampilkan status dalam format JSON:

`sudo aa-status --json`

- Tampilkan status dalam format JSON yang rapi (pretty):

`sudo aa-status --pretty-json`

- Tampilkan jumlah kebijakan yang dimuat:

`sudo aa-status --profiled`

- Tampilkan jumlah kebijakan _enforce_ yang dimuat:

`sudo aa-status --enforced`

- Tampilkan jumlah kebijakan _non-enforce_ yang dimuat:

`sudo aa-status --complaining`

- Tampilkan jumlah kebijakan _enforce_ yang dimuat yang mematikan tugas:

`sudo aa-status --kill`
