# dtc

> Device Tree Compiler-ը, սարքի ծառերը ձևաչափերի միջև վերակազմավորելու գործիք:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/dtc>:.

- Կազմել սարքի ծառի աղբյուրը `.dts` ֆայլը երկուական սարքի ծառի բլբի `.dtb` ֆայլի մեջ:

`dtc -I dts -O dtb -o {{path/to/output_file.dtb}} {{path/to/input_file.dts}}`

- Կազմեք սարքի ծառի աղբյուրը `.dts` ֆայլը երկուական սարքի ծառի բլբի ծածկույթի `.dtbo` ֆայլի մեջ:

`dtc -@ -I dts -O dtb -o {{path/to/output_file.dtbo}} {{path/to/input_file.dts}}`

- Սարքի ծառի բլբի `.dtb` ֆայլը ապակոմպիլացրեք ընթեռնելի սարքի ծառի աղբյուրի `.dts` ֆայլի մեջ:

`dtc -I dtb -O dts -o {{path/to/output_file.dts}} {{path/to/input_file.dtb}}`

- Ապակոմպիլացրեք ընթացիկ սարքի ծառը համակարգից ընթեռնելի սարքի ծառի աղբյուրի `.dts` ֆայլի մեջ.:

`dtc -I fs -O dts /proc/device-tree`
