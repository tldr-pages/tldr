# zipalign

> Ensures that all uncompressed files in the archive are aligned relative to the start of the file.
> More information: https://developer.android.com/studio/command-line/zipalign.

- To align `infile.apk` and save it as `outfile.apk`:

`zipalign -p -f -v 4 infile.apk outfile.apk`

- To confirm the alignment of `existing.apk`:

`zipalign -c -v 4 existing.apk`
