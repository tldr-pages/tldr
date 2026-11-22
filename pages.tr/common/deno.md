# deno

> JavaScript, TypeScript ve WebAssembly için güvenli bir çalışma zamanı ortamı.
> `npm` veya `jsr` kullanan bağımlılık yönetiminin yanı sıra bench, bundle, doc ve coverage gibi araçlar içerir.
> Daha fazla bilgi: <https://docs.deno.com/runtime/reference/cli/>.

- Bir REPL (etkileşimli kabuk) başlat:

`deno`

- Örnek adlı yeni bir proje başlat ve test et:

`deno init {{örnek}} && cd {{örnek}} && deno test`

- Bir dosyayı güvenli bir şekilde çalıştır (gerekirse ağ, okuma vb. izinleri soracaktır):

`deno run {{dosya/yolu.ts}}`

- Açık izinlerle veya tüm izinleri vererek bir dosyayı çalıştır (yalnızca kaynağa güveniyorsanız):

`deno run {{--allow-env|--allow-net|--allow-write|--allow-all}} {{jsr:@deno/deployctl}}`

- Mevcut `deno.json` içindeki görevleri veya `package.json` içindeki betikleri listele ve çalıştır:

`deno task`

- Mevcut `deno.json` veya `package.json` dosyasında listelenen bağımlılıkları yükle:

`deno install`

- Türleri denetle, biçimlendir ve lint uygula (mümkünse düzelt):

`deno check && deno fmt && deno lint --fix`

- Betiği, içe aktarılan bağımlılıkları ve çalışma zamanını bağımsız tek bir yürütülebilir dosyada derle:

`deno compile {{dosya/yolu.ts}}`
