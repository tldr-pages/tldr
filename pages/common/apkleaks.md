# apkleaks

> Expose URIs, endpoints, and secrets from APK files.
> Note: APKLeaks utilizes the `jadx` disassembler to decompile APK files.
> More information: <https://github.com/dwisiswant0/apkleaks>.

- Scan an APK [f]ile for URIs, endpoints, and secrets:

`apkleaks --file {{path/to/file.apk}}`

- Scan and save the [o]utput to a specific file:

`apkleaks --file {{path/to/file.apk}} --output {{path/to/output.txt}}`

- Pass `jadx` disassembler [a]rguments:

`apkleaks --file {{path/to/file.apk}} --args "{{--threads-count 5 --deobf}}"`
