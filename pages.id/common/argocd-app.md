# argocd app

> Program baris perintah untuk mengatur aplikasi bersama Argo CD.
> Informasi lebih lanjut: <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd_app/>.

- Dapatkan daftar aplikasi yang diatur bersama Argo CD:

`argocd app list --output {{json|yaml|wide}}`

- Lihat informasi mengenai suatu aplikasi:

`argocd app get {{nama_aplikasi}} --output {{json|yaml|wide}}`

- Sebarkan (deploy) aplikasi secara internal (ke dalam klaster yang sama dengan yang dijalankan Argo CD):

`argocd app create {{nama_aplikasi}} --repo {{alamat_url_repositori_dalam_git}} --path {{jalan/menuju/repo}} --dest-server https://kubernetes.default.svc --dest-namespace {{ns}}`

- Hapus suatu aplikasi:

`argocd app delete {{nama_aplikasi}}`

- Aktifkan fitur sinkronisasi otomatis dalam suatu aplikasi:

`argocd app set {{nama_aplikasi}} --sync-policy auto --auto-prune --self-heal`

- Pratinjau hasil proses sinkronisasi aplikasi tanpa berdampak kepada klaster yang berjalan (dry-run):

`argocd app sync {{nama_aplikasi}} --dry-run --prune`

- Tampilkan riwayat penyebaran (deployment) aplikasi:

`argocd app history {{nama_aplikasi}} --output {{wide|id}}`

- Batalkan penyebaran dengan memuat (rollback) versi hasil sebaran sebelumnya (dan menghapus sumber daya baru yang tak diduga), berdasarkan nomor induk (ID) riwayat:

`argocd app rollback {{nama_aplikasi}} {{id_riwayat}} --prune`
