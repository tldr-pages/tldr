# chatgpt

> Skrip syel untuk memakai OpenAI ChatGPT dan DALL-E dalam terminal.
> Informasi lebih lanjut: <https://github.com/0xacx/chatGPT-shell-cli>.

- Jalankan dalam mode percakapan interaktif:

`chatgpt`

- Berikan [p]rompt (pertanyaan) untuk dijawab oleh sang model:

`chatgpt {{[-p|--prompt]}} "{{Bagaimana cara membuat kriteria ekspresi reguler untuk mencocokkan format alamat surel/email?}}"`

- Jalankan dalam mode interaktif menggunakan suatu [m]odel (model default adalah `gpt-3.5-turbo`):

`chatgpt {{[-m|--model]}} {{gpt-4}}`

- Jalankan dalam mode interaktif dengan [i]nitial prompt, perintah/permintaan awal yang dapat mendefinisikan jenis jawaban yang diharapkan dari sang model:

`chatgpt {{[-i|--init-prompt]}} "{{Anda adalah Rick, dari serial Rick and Morty. Tanggapi pertanyaan dengan gayanya dan menyertakan lelucon yang menghina.}}"`

- Alihkan luaran dari program baris perintah lainnya sebagai pertanyaan masukan (prompt) kepada `chatgpt`:

`echo "{{Bagaimana cara melihat proses yang berjalan di Ubuntu?}}" | chatgpt`

- Generate an image using DALL-E:

`chatgpt {{[-p|--prompt]}} "{{image: Seekor kucing putih}}"`
