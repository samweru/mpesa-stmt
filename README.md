Mpesa Statement Extraction
===

This application is used to extract MPESA `pdf` statement to `csv` in an orderly format.

### Disclaimer

Remove PDF password at your own **RISK** but this is required to run this/these script(s).
Below is a script to remove password from your PDF.

```sh
# sudo apt install qpdf
qpdf --password='YOUR_CURRENT_PASSWORD' --decrypt input.pdf output.pdf
```

### Requirements

```sh
pip install opencv-python
pip install camelot-py
pip install pandas openpyxl
```

### Usage

```sh
# ./bin/run <pdf_file>
./bin/run 2025.pdf
```

Your resulting `output.csv` is the final product. 
You may want to review and clean your `output.csv` but the hassle is much less after this process.

### Note

If your want to change/omit `--skip` document sheets and/or omit  `--drop-first-col` you can do that in `bin/merge-sheets` script.