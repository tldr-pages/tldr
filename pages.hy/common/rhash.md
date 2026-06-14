#ռաշ

> Հաշվեք կամ ստուգեք ընդհանուր հաղորդագրությունների ամփոփումները:.
> Լրացուցիչ տեղեկություններ. <https://rhash.sourceforge.io/manpage.php>:.

- Հաշվեք ֆայլի լռելյայն CRC32 ամփոփումները.:

`rhash {{path/to/file}}`

- Ռեկուրսիվ կերպով մշակեք գրացուցակը SFV ֆայլ ստեղծելու համար՝ օգտագործելով SHA1:

`rhash --sha1 --recursive {{path/to/folder}} > {{path/to/output.sfv}}`

- Ստուգեք SFV ֆայլի հիման վրա ֆայլերի ամբողջականությունը.:

`rhash --check {{path/to/file.sfv}}`

- Հաշվեք տեքստային հաղորդագրության SHA3 ամփոփումը.:

`rhash --sha3-256 --message '{{message}}'`

- Հաշվեք CRC32 ֆայլի ամփոփումը և ելքագրեք base64-ում կոդավորված՝ օգտագործելով BSD ձևաչափը.:

`rhash --base64 --bsd {{path/to/file}}`

- Օգտագործեք մաքսային ելքային ձևանմուշ.:

`rhash --printf '{{%p\t%s\t%{mtime}\t%m\n}}' {{path/to/file}}`
