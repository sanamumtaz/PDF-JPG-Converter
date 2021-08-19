# PDF-JPG-Converter
PDF ⇔ JPG converter - Python 3


### Packages Used
- [pdf2image](https://pypi.org/project/pdf2image/) for PDF to JPG conversion.
- [img2pdf](https://pypi.org/project/img2pdf/) for JPG/JPEG to PDF conversion.

**GUI made using [PAGE](https://sourceforge.net/projects/page/)**

### Run the program
- Download the scripts
- **Download Poppler**
  - **For Windows:** Download ZIP file [@oschwartz10612 version](https://github.com/oschwartz10612/poppler-windows/releases/). Extract it and place `bin` folder in the same directory as the scripts.
  - **For MAC:** Download from [store](https://macappstore.org/poppler/).
  - **For Linux:** Most distros ship with `pdftoppm` and `pdftocairo`. If they are not installed, refer to your package manager to install `poppler-utils`.
- Run `python pdf_jpg_converter.py`

| ![JPG to PDF](https://user-images.githubusercontent.com/35191030/130137429-60b1ef67-239d-484d-88f4-a8c0d66d638b.png) | ![PDF to JPG](https://user-images.githubusercontent.com/35191030/130140223-e3041cf0-7ba4-4e7d-be34-434e561c7f4d.png) | ![Successful conversion](https://user-images.githubusercontent.com/35191030/130138374-64e84b9c-c69b-465a-b70c-2290bc2b4ad3.png) |
|:--:|:--:|:--:|
|<i>JPG to PDF</i>|<i>PDF to JPG</i>|<i>Successful conversion</i>|

</br>**Enjoy converting your documents without risking privacy :)**

*You can create executable file using [PyInstaller](https://www.pyinstaller.org/)*
