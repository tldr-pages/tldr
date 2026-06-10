#ֆիո

> Ճկուն I/O փորձարկիչ. կատարել I/O գործողություն, որը ներառում է բազմաթիվ թելեր կամ գործընթացներ:.
> Լրացուցիչ տեղեկություններ. <https://fio.readthedocs.io/en/latest/fio_doc.html>:.

- Պատահական թեստը կարդում է.:

`fio --filename={{path/to/file}} --direct=1 --rw=randread --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly`

- Փորձարկման հաջորդականությունը ասվում է.:

`fio --filename={{path/to/file}} --direct=1 --rw=read --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1 --readonly`

- Փորձարկել պատահական կարդալ/գրել.:

`fio --filename={{path/to/file}} --direct=1 --rw=randrw --bs=4k --ioengine=libaio --iodepth=256 --runtime=120 --numjobs=4 --time_based --group_reporting --name={{job_name}} --eta-newline=1`

- Փորձարկեք աշխատանքի ֆայլի պարամետրերով.:

`fio {{path/to/job_file}}`

- Փոխակերպեք կոնկրետ աշխատանքի ֆայլը հրամանի տողի ընտրանքների.:

`fio --showcmd {{path/to/job_file}}`
