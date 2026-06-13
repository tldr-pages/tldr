# pnmgamma

> Perform gamma correction on PNM images.
> More information: <https://netpbm.sourceforge.net/doc/pnmgamma.html>.

- Convert the image from BT.709 luminance to radiance or sRGB luminance:

`pnmgamma -{{bt709tolinear|bt709tosrgb}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Convert the image from radiance or sRGB luminance to BT.709 luminance:

`pnmgamma -{{lineartobt709|srgbtobt709}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Specify the gamma value used for the gamma transfer function:

`pnmgamma {{[-ga|-gamma]}} {{value}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Specify the gamma value used for the gamma transfer function per color component:

`pnmgamma {{[-rg|-rgamma]}} {{value}} {{[-gg|-ggamma]}} {{value}} {{[-bg|-bgamma]}} {{value}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
