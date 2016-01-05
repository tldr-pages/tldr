# 7za

> A file archiver with high compression ratio

- compress directory or file

`7za a {{compressed.7z}} {{directory_or_file_to_compress}}`

- decompress an existing 7z file with original directory structure

`7za x {{compressed.7z}}`

- compress to zip format

`7za a -tzip {{compressed.zip}} {{directory_or_file_to_compress}}`

- create multipart 7zip file; `part_size` specifies part size in Bytes, Kilobytes, Megabytes or Gigabytes.

`7za -v{{part_size}}{{[b|k|m|g]}} {{compressed.7z}} {{directory_or_file_to_compress}}`
