# 7zr

> A file archiver with high compression ratio.
> A standalone version of `7z` that only supports .7z files.

- Compress directory or file:

`7zr a {{compressed.7z}} {{directory_or_file_to_compress}}`

- Decompress an existing 7z file with original directory structure:

`7zr x {{compressed.7z}}`

- Create multipart 7zip file; `part_size` specifies part size in Bytes, Kilobytes, Megabytes or Gigabytes:

`7zr -v{{part_size}}{{[b|k|m|g]}} {{compressed.7z}} {{directory_or_file_to_compress}}`
