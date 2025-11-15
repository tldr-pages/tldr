# aws accessanalyzer

> Analisa dan tinjau ulang kebijakan penggunaan sumber daya untuk melihat potensi risiko keamanan.
> Informasi lebih lanjut: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html>.

- Buat suatu instansi Access Analyzer:

`aws accessanalyzer create-analyzer --analyzer-name {{nama_analyzer}} --type {{tipe_analisis}} --tags {{daftar_tag}}`

- Hapus suatu instansi Access Analyzer:

`aws accessanalyzer delete-analyzer --analyzer-arn {{arn_analyzer}}`

- Tampilkan rincian tentang suatu instansi Access Analyzer:

`aws accessanalyzer get-analyzer --analyzer-arn {{arn_analyzer}}`

- Tampilkan daftar seluruh instansi Access Analyzers:

`aws accessanalyzer list-analyzers`

- Mutakhirkan suatu aturan terhadap instansi Access Analyzer:

`aws accessanalyzer update-analyzer --analyzer-arn {{arn_analyzer}} --tags {{daftar_tag_baru}}`

- Buat sebuah aturan bagi proses pengarsipan terhadap instansi Access Analyzer:

`aws accessanalyzer create-archive-rule --analyzer-arn {{arn_analyzer}} --rule-name {{nama_aturan}} --filter {{filter}}`

- Hapus suatu aturan pengarsipan bagi instansi Access Analyzer:

`aws accessanalyzer delete-archive-rule --analyzer-arn {{arn_analyzer}} --rule-name {{nama_aturan}}`

- Tampilkan daftar seluruh aturan pengarsipan yang berlaku bagi suatu instansi Access Analyzer:

`aws accessanalyzer list-archive-rules --analyzer-arn {{arn_analyzer}}`
