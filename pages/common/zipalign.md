# zipalign

> Zip archive alignment tool.
> More information: https://developer.android.com/studio/command-line/zipalign.

- Align the data of a ZIP file on {{number}} bytes:

`zipalign {{number}} {{path/to/input.zip}} {{path/to/output.zip}}`

- Check that a ZIP file is correctly aligned on {{number}} bytes:

`zipalign -v -c {{number}} {{path/to/input.zip}}`
