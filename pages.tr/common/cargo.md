# cargo

> Rust projelerini ve modül bağımlılıklarını (crate'leri) yönet.
> `build` gibi bazı alt komutların kendi kullanım dokümantasyonu vardır.
> Daha fazla bilgi için: <https://doc.rust-lang.org/stable/cargo/>.

- Crate ara:

`cargo search {{arama_ifadesi}}`

- Çalıştırılabilir bir crate yükle:

`cargo install {{crate_adı}}`

- Yüklü çalıştırılabilir crate'leri listele:

`cargo install --list`

- Belirtilen dizinde (varsayılan olarak geçerli çalışma dizininde) yeni bir çalıştırılabilir ya da kütüphane Rust projesi oluştur:

`cargo init --{{bin|lib}} {{yol/dizin}}`

- Geçerli dizindeki `Cargo.toml` dosyasına bir bağımlılık ekle:

`cargo add {{bağımlılık}}`

- Geçerli dizindeki Rust projesini release profiliyle derle:

`cargo {{[b|build]}} {{[-r|--release]}}`

- Derlenmiş çalıştırılabilir dosyayı çalıştır (henüz derlenmemişse önce derler):

`cargo {{[r|run]}}`

- Geçerli dizindeki Rust projesini nightly derleyiciyle derle (`rustup` gerektirir):

`cargo +nightly {{[b|build]}}`
