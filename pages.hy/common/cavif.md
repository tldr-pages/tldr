#խավիֆ

> Փոխարկել PNG/JPEG պատկերները AVIF-ի: Գրված է Rust-ով։
> Տես նաև՝ `convert`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/kornelski/cavif-rs>:.

- Փոխակերպեք JPEG ֆայլը AVIF-ի` պահպանելով այն `file.avif`:

`cavif {{path/to/image.jpg}}`

- Կարգավորեք պատկերի որակը և փոխարկեք PNG ֆայլը AVIF-ի.:

`cavif --quality {{1..100}} {{path/to/image.png}}`

- Նշեք ելքի գտնվելու վայրը.:

`cavif {{path/to/image.jpg}} --output {{path/to/output.avif}}`

- Վերագրեք նպատակակետի ֆայլը, եթե այն արդեն գոյություն ունի.:

`cavif --overwrite {{path/to/image.jpg}}`
