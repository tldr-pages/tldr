# pnmpsnr

> Compute the difference between two images.
> More information: <https://netpbm.sourceforge.net/doc/pnmpsnr.html>.

- Compute the difference, i.e. the peak signal-to-noise ratio (PSNR) between two images:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}}`

- Compare the color components rather than the luminance and chrominance components of the images:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -rgb`

- Run in comparison mode, i.e. only output `nomatch` or `match` depending on whether the computing PSNR exceeds `n` or not:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -target {{n}}`

- Run in comparison mode and compare the individual image components, i.e. Y, Cb, and Cr, to the corresponding thresholds:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -target1 {{threshold_Y}} -target2 {{threshold_Cb}} -target3 {{threshold_Cr}}`

- Run in comparison mode and compare the individual image components, i.e. red, green, and blue to the corresponding thresholds:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -rgb -target1 {{threshold_red}} -target2 {{threshold_green}} -target3 {{threshold_blue}}`

- Produce machine-readable output:

`pnmpsnr {{path/to/file1.pnm}} {{path/to/file2.pnm}} -machine`
