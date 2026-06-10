# pv

> Դիտեք տվյալների առաջընթացը խողովակի միջոցով:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/pv>:.

- Տպեք ֆայլի բովանդակությունը և ցուցադրեք առաջընթացի տողը.:

`pv {{path/to/file}}`

- Չափել խողովակների միջև տվյալների հոսքի արագությունն ու քանակը (`--size` պարտադիր չէ).:

`{{command1}} | pv {{[-s|--size]}} {{expected_amount_of_data_for_eta}} | {{command2}}`

- Զտեք ֆայլը, տեսեք և՛ առաջընթացը, և՛ ելքային տվյալների քանակը.:

`pv {{[-cN|--cursor --name]}} in {{path/to/file.txt}} | grep {{pattern}} | pv {{[-cN|--cursor --name]}} out > {{path/to/filtered_file.txt}}`

- Կցեք արդեն գործող գործընթացին և տեսեք դրա ֆայլի ընթերցման առաջընթացը.:

`pv {{[-d|--watchfd]}} {{pid}}`

- Կարդացեք սխալ ֆայլ, բաց թողեք սխալները, ինչպես կկատարեր `dd conv=sync,noerror`:

`pv {{[-EE|--skip-errors --skip-errors]}} {{path/to/faulty_media}} > {{path/to/image.img}}`

- Դադարեցրեք կարդալը նշված քանակի տվյալներ կարդալուց հետո, արագության սահմանաչափը մինչև 1K/վ:

`pv {{[-L|--rate-limit]}} {{1K}} {{[-S|--stop-at-size]}} {{maximum_file_size_to_be_read}}`

- Հաշվեք մեծ ֆայլի հեշը (MD5, SHA1, SHA256 և այլն) և ցույց տվեք առաջընթացը.:

`pv {{path/to/file}} | {{sha256sum}}`
