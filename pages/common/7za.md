# 7za

> A file archiver with highest compression ratio

- package and compress directory or file

`7za a {{compressed.7z}} {{directory_or_file}}`

- decompress an existing 7z file

`7za x {{compressed.7z}}`

- compress to zip format

`7za a  -tzip {{compressed.zip}} {{directory_or_file}}`

- create multipart 7zip file

`7za -v{{size}}{{[b|k|m|g]}} {{compressed.7z}} {{directory_or_file}}`
