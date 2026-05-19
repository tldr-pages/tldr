# iexpress

> Create self-extracting archive executable (`.exe`) or cabinet (`.cab`) files.
> More information: <https://ss64.com/nt/iexpress.html>.

- Build a self-extracting ZIP archive from a given SED file:

`iexpress /n {{path\to\file.sed}}`

- Run the build process in a [m]inimized window:

`iexpress /m {{path\to\file.sed}}`

- Run the build process in a [q]uiet mode, assuming the user account invoking this command as an [a]dministrator or regular [u]ser:

`iexpress /q:{{a|u}} {{path\to\file.sed}}`

- Ensure the `.exe` file to [a]sk, [n]ever, or alway[s] [r]estart the computer after installation:

`iexpress /r:{{a|n|s}} {{path\to\file.sed}}`
