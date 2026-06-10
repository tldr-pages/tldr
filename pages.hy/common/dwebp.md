# dwebp

> `dwebp`-ն ապասեղմում է WebP ֆայլերը PNG, PAM, PPM կամ PGM պատկերների:.
> Անիմացիոն WebP ֆայլերը չեն աջակցվում:.
> Լրացուցիչ տեղեկություններ. <https://developers.google.com/speed/webp/docs/dwebp/>:.

- Փոխակերպեք WebP ֆայլը PNG ֆայլի.:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}}`

- Փոխակերպեք WebP ֆայլը որոշակի ֆայլի տեսակի.:

`dwebp {{path/to/input.webp}} -bmp|-tiff|-pam|-ppm|-pgm|-yuv -o {{path/to/output}}`

- Փոխակերպեք WebP ֆայլը, հնարավորության դեպքում օգտագործելով բազմաշերտ.:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -mt`

- Փոխակերպեք WebP ֆայլը, բայց միևնույն ժամանակ կտրեք և չափեք.:

`dwebp {{input.webp}} -o {{output.png}} -crop {{x_pos}} {{y_pos}} {{width}} {{height}} -scale {{width}} {{height}}`

- Փոխակերպեք WebP ֆայլը և շրջեք ելքը.:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -flip`

- Փոխակերպեք WebP ֆայլը և մի օգտագործեք միջանցքային զտիչ՝ ապակոդավորման գործընթացը արագացնելու համար.:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -nofilter`
