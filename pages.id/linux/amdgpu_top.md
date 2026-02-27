# amdgpu_top

> Tool untuk menampilkan penggunaan GPU AMD dan metrik perangkat keras menggunakan driver AMDGPU.
> Lihat juga: `nvtop`, `radeontop`.
> Informasi lebih lanjut: <https://github.com/Umio-Yasuno/amdgpu_top#usage>.

- Tampilkan daftar perangkat AMDGPU:

`amdgpu_top --list`

- Lakukan dump semua proses GPU dan penggunaan memori per-proses:

`amdgpu_top {{[-p|--process]}}`

- Pilih GPU spesifik berdasarkan bus PCI:

`amdgpu_top --pci "{{0000:01:00.0}}"`

- Jalankan monitor TUI interaktif:

`amdgpu_top`

- Jalankan monitor GUI:

`amdgpu_top --gui`

- Jalankan tampilan TUI sederhana mirip SMI:

`amdgpu_top --smi`
