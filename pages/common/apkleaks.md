# apkleaks

> Expose URIs, endpoints, and secrets from APK files.
> Note: APKLeaks utilizes the `jadx` disassembler to decompile APK files.
> More information: <https://github.com/dwisiswant0/apkleaks>.

- Scan an APK file for URIs, endpoints, and secrets:

`apkleaks {{[-f|--file]}} {{path/to/file.apk}}`

- Scan and save the output to a specific file:

`apkleaks {{[-f|--file]}} {{path/to/file.apk}} {{[-o|--output]}} {{path/to/output.txt}}`

- Pass `jadx` disassembler arguments:

`apkleaks {{[-f|--file]}} {{path/to/file.apk}} {{[-a|--args]}} "{{--threads-count 5 --deobf}}"`
