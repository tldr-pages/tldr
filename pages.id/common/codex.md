# codex

> Asisten kode berbasis bahasa alami untuk terminal, ditenagai oleh OpenAI.
> Membaca dan mengubah berkas-berkas di dalam direktori saat ini untuk memenuhi permintaan.
> Informasi lebih lanjut: <https://developers.openai.com/codex/cli/reference>.

- Mulai sesi interaktif Codex di dalam direktori saat ini:

`codex`

- Jalankan satu perintah Codex menggunakan sebuah instruksi (prompt):

`codex "{{prompt}}"`

- Jalankan perintah dengan mengizinkan Codex mengubah berkas-berkas di dalam ruang kerja (workspace):

`codex --sandbox workspace-write "{{prompt}}"`

- Gunakan model spesifik:

`codex {{[-m|--model]}} {{nama_model}} "{{prompt}}"`

- Gunakan penyedia model sumber terbuka (open-source) lokal:

`codex --oss --local-provider {{lmstudio|ollama}} "{{prompt}}"`

- [Interaktif] Tampilkan konfigurasi sesi dan penggunaan token:

`/status`

- Tampilkan bantuan:

`codex {{[-h|--help]}}`
