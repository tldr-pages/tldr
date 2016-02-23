# 7za

> A file archiver with high compression ratio.
> A standalone version of `7z` with support for fewer archive types.

- Archive a file or folder:

`7za a {{compressed.7z}} {{path/to/file}}`

- Extract an existing 7z file with original directory structure:

`7za x {{compressed}}`

- Archive using a specific archive type:

`7za a -t{{7z|zip|gzip|bzip2|tar}} {{compressed}} {{path/to/file}}`

- List the contents of an archive file:

`7za l {{compressed}}`
