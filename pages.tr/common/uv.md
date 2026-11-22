# uv

> Hızlı bir Python paket ve proje yöneticisi.
> `tool`, `python` vb. bazı alt komutların kendi kullanım dokümantasyonu vardır.
> Daha fazla bilgi için: <https://docs.astral.sh/uv/reference/cli/>.

- Geçerli dizinde yeni bir Python projesi oluştur:

`uv init`

- Belirtilen yolda yeni bir Python projesi oluştur:

`uv init {{yol/dizin}}`

- Projeye yeni bir bağımlılık ekle:

`uv add {{paket}}`

- Projeden bir bağımlılığı kaldır:

`uv remove {{paket}}`

- Projenin ortamında bir betik veya komut çalıştır:

`uv run {{yol/betik.py|komut}}`

- Projenin ortamını `pyproject.toml` dosyasından güncelle:

`uv sync`

- Projenin bağımlılıkları için bir kilit dosyası oluştur:

`uv lock`

- Projeyi kaynak ve ikili dağıtım paketlerine derle:

`uv build`
