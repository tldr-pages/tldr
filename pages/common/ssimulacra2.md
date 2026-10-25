# ssimulacra2

> Score how visually similar a distorted image is to its original.
> Scores range from negative (very strong distortion) through 90 (visually lossless) to 100 (mathematically lossless).
> More information: <https://github.com/cloudinary/ssimulacra2#usage>.

- Score a distorted image against the original (both images must have the same dimensions):

`ssimulacra2 {{path/to/original.png}} {{path/to/distorted.png}}`

- Display the usage and what each score range means:

`ssimulacra2`
