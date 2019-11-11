# zipalign

> Zip archive alignment tool.
> More information: <https://developer.android.com/studio/command-line/zipalign>.

- Align the data of a ZIP file on {{4}} bytes:

`zipalign {{4}} {{path/to/input.zip}} {{path/to/output.zip}}`

- Check that a ZIP file is correctly aligned on {{4}} bytes:

`zipalign -v -c {{4}} {{path/to/input.zip}}`
