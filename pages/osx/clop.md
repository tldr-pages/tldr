# clop

> Optimise, crop, downscale, convert, and manipulate images, videos, and PDFs.
> More info: <https://lowtechguys.com/clop/>

- Optimise images, videos, or PDFs:
  ```sh
  clop optimise path/to/file
  ```

- Aggressive optimisation on multiple files:
  ```sh
  clop optimise -a path/to/file1 path/to/file2
  ```

- Optimise all files in a folder recursively:
  ```sh
  clop optimise -r path/to/folder
  ```

- Optimise only specific types (e.g., jpeg, png):
  ```sh
  clop optimise --types jpeg,png path/to/folder
  ```

- Downscale an image or video by 50%:
  ```sh
  clop downscale --factor 0.5 path/to/file
  ```

- Crop an image, video, or PDF to a specific size:
  ```sh
  clop crop --size 1200x630 path/to/file
  ```

- Smart crop by centering on features:
  ```sh
  clop crop --smart-crop --size 1200x630 path/to/file
  ```

- Convert images to WebP format:
  ```sh
  clop convert --format webp path/to/image.png
  ```

- Crop PDFs to a specific aspect ratio (non-destructive):
  ```sh
  clop crop-pdf --aspect-ratio 16:9 path/to/document.pdf
  ```

- Restore original size to a cropped PDF:
  ```sh
  clop uncrop-pdf path/to/document.pdf
  ```

- Remove EXIF metadata from images and videos:
  ```sh
  clop strip-exif path/to/file
  ```

- Show help for a subcommand:
  ```sh
  clop help <subcommand>
  ```
