#լմմս

> Անվճար, բաց կոդով, միջպլատֆորմային թվային աուդիո աշխատանքային կայան:.
> Արտադրեք `.mmp` կամ `.mmpz` նախագծի ֆայլը, թափեք `.mmpz`-ը որպես XML կամ գործարկեք GUI-ը:.
> Տես նաև՝ `mixxx`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/lmms>:.

- Սկսեք GUI-ն.:

`lmms`

- Սկսեք GUI-ն և բեռնեք արտաքին կազմաձևը.:

`lmms {{[-c|--config]}} {{path/to/config.xml}}`

- Սկսեք GUI-ն և ներմուծեք MIDI կամ Hydrogen ֆայլ.:

`lmms --import {{path/to/midi_or_hydrogen_file}}`

- Սկսեք GUI-ն նշված պատուհանի չափով.:

`lmms --geometry {{x_size}}x{{y_size}}+{{x_offset}}+{{y_offset}}`

- Թափել `.mmpz` ֆայլը՝:

`lmms dump {{path/to/mmpz_file.mmpz}}`

- Ներկայացրեք նախագծի ֆայլը.:

`lmms render {{path/to/mmpz_or_mmp_file}}`

- Ներկայացրեք նախագծի ֆայլի առանձին հետքերը.:

`lmms rendertracks {{path/to/mmpz_or_mmp_file}} {{path/to/dump_directory}}`

- Պատվիրեք սովորական նմուշի չափով, ձևաչափով և որպես հանգույց.:

`lmms render {{[-s|--samplerate]}} {{88200}} {{[-f|--format]}} {{ogg}} {{[-l|--loop]}} {{[-o|--output]}} {{path/to/output_file.ogg}}`
