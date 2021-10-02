# caffeinate

> Menghindari macOS dari sleep (mode tidur).
> Informasi lebih lanjut: <https://ss64.com/osx/caffeinate.html>.

- Menghindari mode sleep selama 1 jam (3600 detik):

`caffeinate -u -t {{3600}}`

- Menghindari mode sleep sampai sebuah command selesai:

`caffeinate -s {{command}}`

- Menghindari mode sleep sampai anda mengetik Ctrl-C:

`caffeinate -i`
