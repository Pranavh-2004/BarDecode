# BarDecode

BarDecode is a simple barcode reader project that can read barcodes from both images and webcam video streams. It uses Python's `opencv-python` for image processing and `pyzbar` for barcode decoding. The project demonstrates two modes: reading barcodes from an image file or live from a webcam.

## Features

- **Barcode Detection**: Detects and decodes barcodes from images and live camera feeds.
- **Image Processing**: Displays the decoded barcode with a rectangle drawn around it for easy identification.
- **Support for Various Barcode Types**: Can read various barcode types such as EAN13, QR code, UPC, etc.

## Installation

### 1. **Install Zbar Library**

`pyzbar` depends on the `zbar` library to decode barcodes. You need to install `zbar` on your macOS machine.

To install `zbar`, you can use Homebrew with the following command:

```bash
brew install zbar
```

This will install the zbar library, which is required by pyzbar to function correctly.

### 2. **Clone the repository**

```bash
git clone https://github.com/yourusername/BarDecode.git
cd BarDecode
```

### 3. **Set up a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4. **Install the dependencies:**

Install the necessary Python libraries with:

```bash
pip install -r requirements.txt
```

The required packages are:

- opencv-python - For image processing and displaying the barcode in images.
- pyzbar - For decoding barcodes from images.

## Usage

You can run the project in two modes:

### 1. **Reading from an Image**

To read barcodes from an image, call the read_barcode_from_image() function and provide the image path.

```bash
read_barcode_from_image('path_to_image_file.png')
```

It will display the image with a rectangle drawn around the barcode and output the decoded barcode data to the console.

### 2. **Reading from the Webcam**

To read barcodes in real-time using your webcam, call the read_barcode_from_camera() function.

```bash
read_barcode_from_camera()
```

Press ‘q’ to exit the webcam feed.

## Example

### Reading Barcode from an Image:

```bash
python main.py
```

The output will look like:

```plaintext
Decoded Barcode: 1234567890128 (Type: EAN13)
```

### Reading Barcode from Webcam:

Run the following command:

```bash
python main.py
```

The webcam will start, and you can scan barcodes in real time. Press ‘q’ to stop the webcam feed.

## Contributing

Feel free to fork the repository, create a branch, make changes, and create a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
