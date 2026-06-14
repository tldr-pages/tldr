# կռունկի քաշում

> Քաշեք հեռավոր պատկերները հղումով և պահեք դրանց բովանդակությունը տեղում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_pull.md>:.

- Քաշեք հեռավոր պատկերը.:

`crane pull {{image_name}} {{path/to/tarball}}`

- Պահպանել պատկերի հղումը, որն օգտագործվում է որպես ծանոթագրություն, երբ օգտագործվում է `--format=oci`-ով:

`crane pull {{image_name}} {{path/to/tarball}} --annotate-ref`

- Պատկերի շերտերի քեշի ուղին.:

`crane pull {{image_name}} {{path/to/tarball}} {{[-c|--cache_path]}} {{path/to/cache}}`

- Պատկերները պահելու ձևաչափ (կանխադրված `tarball`):

`crane pull {{image_name}} {{path/to/tarball}} {{-format}} {{format_name}}`

- Ցուցադրել օգնությունը.:

`crane pull {{[-h|--help]}}`
