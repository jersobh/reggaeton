# Reggaeton

Reggaeton is a visual regression tool designed to compare two images and highlight the differences with a visual indication. It's particularly useful for identifying changes or anomalies in visual content over time or between versions.

## Example
### Images to be compared

<img src="https://raw.githubusercontent.com/jersobh/reggaeton/master/original.png" alt="Original image" width="450" />
<br />
<img src="https://raw.githubusercontent.com/jersobh/reggaeton/master/modified.png" alt="Modified image" width="450" />

### Output image

<img src="https://raw.githubusercontent.com/jersobh/reggaeton/master/output.png" alt="Output image" width="450" />

## Installation

You can install Reggaeton directly from PyPI:

```bash
pip install reggaeton
```

This command will install Reggaeton and its dependencies.

# Usage
Reggaeton can be used both as a library in your Python scripts and as a command-line tool.

## As a Command-Line Tool
After installation, you can use Reggaeton directly from your terminal:

```bash
reggaeton path/to/before/image.jpg path/to/after/image.jpg path/to/output/image.jpg
```
This command compares before and after images and saves the output image with differences highlighted to the specified path.

## As a Library
You can also use Reggaeton in your Python scripts:

```python
from reggaeton import compare_images

result_image = compare_images('path/to/before.jpg', 'path/to/after.jpg')
if result_image is not None:
    # Save or process result_image as needed
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request.

## License
Reggaeton is released under the MIT License. See the LICENSE file for more details.