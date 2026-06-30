Mpesa Statement Extraction
===

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