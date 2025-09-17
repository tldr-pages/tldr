# mkvpropedit

> Modify properties of existing Matroska files without a complete remux.
> More information: <https://mkvtoolnix.download/doc/mkvpropedit.html>.

- Delete title:

`mkvpropedit {{[-d|--delete]}} title {{path/to/file.mkv}}`

- Mark subtitle track 3 as SDH - Subtitles for deaf and hearing impared:

`mkvpropedit {{path/to/file.mkv}} {{[-e|--edit]}} track:s3 {{[-s|--set]}} flag-hearing-impaired=1`

- Mark audio track 2 as Default:

`mkvpropedit {{path/to/file.mkv}} {{[-e|--edit]}} track:a2 {{[-s|--set]}} flag-default=1`

- Delete the name of video track 1:

`mkvpropedit {{path/to/file.mkv}} {{[-e|--edit]}} track:v1 {{[-d|--delete]}} name`
