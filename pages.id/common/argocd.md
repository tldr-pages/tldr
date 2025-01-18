# argocd

> Program baris perintah untuk mengatur suatu peladen (server) Argo CD.
> Beberapa subperintah seperti `argocd app` mempunyai dokumentasi terpisah.
> Informasi lebih lanjut: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

- Masuk (login) ke dalam suatu peladen Argo CD:

`argocd login --insecure --username {{nama_pengguna}} --password {{kata_sandi}} {{peladen_argocd:port}}`

- Dapatkan daftar aplikasi:

`argocd app list`
