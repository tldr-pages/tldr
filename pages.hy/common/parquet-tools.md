# մանրահատակ-գործիքներ

> Ցույց տալ, ստուգել և շահարկել Մանրահատակի ֆայլը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/apache/parquet-java>:.

- Ցուցադրել մանրահատակի ֆայլի բովանդակությունը.:

`parquet-tools cat {{path/to/parquet}}`

- Ցուցադրել մանրահատակի ֆայլի առաջին մի քանի տողերը.:

`parquet-tools head {{path/to/parquet}}`

- Տպել մանրահատակի ֆայլի սխեման.:

`parquet-tools schema {{path/to/parquet}}`

- Տպել մանրահատակի ֆայլի մետատվյալները.:

`parquet-tools meta {{path/to/parquet}}`

- Տպել մանրահատակի ֆայլի բովանդակությունը և մետատվյալները.:

`parquet-tools dump {{path/to/parquet}}`

- Միացրեք մի քանի մանրահատակի ֆայլեր թիրախայինի մեջ.:

`parquet-tools merge {{path/to/parquet1}} {{path/to/parquet2}} {{path/to/target_parquet}}`

- Տպեք տողերի քանակը մանրահատակի ֆայլում.:

`parquet-tools rowcount {{path/to/parquet}}`

- Տպեք մանրահատակի ֆայլի սյունակները և օֆսեթ ինդեքսները.:

`parquet-tools column-index {{path/to/parquet}}`
