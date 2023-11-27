# xcodes runtimes

> Atur pemasangan runtime Simulator yang tersedia bagi aplikasi Xcode.
> Informasi lebih lanjut: <https://github.com/xcodesorg/xcodes>.

- Tampilkan seluruh Simulator yang tersedia bagi aplikasi Xcode:

`xcodes runtimes --include-betas`

- Unduh sebuah runtime Simulator:

`xcodes runtimes download {{nama_runtime}}`

- Unduh dan pasang sebuah runtime Simulator:

`xcodes runtimes install {{nama_runtime}}`

- Unduh/pasang runtime Simulator untuk iOS/watchOS/tvOS/visionOS versi spesifik (nama harus ditulis sebagai case-sensitive):

`xcodes runtimes {{download|install}} "{{iOS|watchOS|tvOS|visionOS}} {{nama_runtime}}"`

- Atur lokasi penyimpanan arsip runtime yang akan diunduh (nilai default: `~/Downloads`):

`xcodes runtimes {{download|install}} {{nama_runtime}} --directory {{jalan/menuju/direktori}}`

- Jangan hapus arsip runtime Simulator setelah pemasangan selesai:

`xcodes runtimes install {{nama_runtime}} --keep-archive`
