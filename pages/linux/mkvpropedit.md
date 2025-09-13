# mkvpropedit

> Modify properties of existing Matroska files without a complete remux.
> More information: <https://mkvtoolnix.download/doc/mkvpropedit.html>.

- Delete title:

`mkvpropedit --delete title {{path/to/mkv_file}}`

- Mark subtitle track 3 as SDH - Subtitles for deaf and hearing impared:

`mkvpropedit {{path/to/mkv_file}} --edit track:s3 --set flag-hearing-impaired=1`

- Mark audio track 2 as Default:

`mkvpropedit {{path/to/mkv_file}} --edit track:a2 --set flag-default=1`

- Delete the name of video track 1:

`mkvpropedit {{path/to/mkv_file}} --edit track:v1 --delete name`
