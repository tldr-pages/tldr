# brew install

> Pasang suatu formula atau cask pada Homebrew.
> Informasi lebih lanjut: <https://docs.brew.sh/Manpage#install-options-formulacask->.

- Pasang suatu formula/cask:

`brew install {{formula|cask}}`

- Bangun dan pasang suatu formula dari kode sumber (seluruh formula yang dibutuhkan tetap akan diunduh sebagai berkas jadian / bottle):

`brew install --build-from-source {{formula}}`

- Unduh manifest dan tampilkan daftar formula/cask yang akan dipasang tanpa melakukannya (dry-run):

`brew install --dry-run {{formula|cask}}`
