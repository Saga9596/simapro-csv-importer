# Simapro LCI Import Converter

A lightweight Python utility that streamlines Life Cycle Inventory (LCI) data ingestion into SimaPro. Simply feed it your raw CSV exports, specify your modules, and it produces a formatted import file—no manual tweaks required.

---

## Key Highlights

- **Effortless Transformation**: Convert raw LCI tables (CSV) directly into SimaPro-compatible imports.
- **Module Selection**: Choose any combination of lifecycle stages (e.g., A1–A4, B6).
- **Automated Mapping**: Smart detection of flow names, units, and categories.
- **Clean Output**: Drops unsupported fields (uncertainty, comments) and retains only what SimaPro needs.

---

## Prerequisites

- Python 3.7 or above
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)

Install dependencies:

```bash
pip install pandas numpy
```

---

## Input Specification

Your input CSV must include these columns:

| Column           | Description                                                |
|------------------|------------------------------------------------------------|
| `Amount`         | Numeric value of the flow                                  |
| `Unit`           | Unit (e.g., `kg`, `m3`, `MJ`)                              |
| `Activity`       | Exact SimaPro dataset or process name (case sensitive)     |
| `Category`       | Flow category (e.g., `Raw`, `Air`, `Water`, `Waste`)       |
| `Stages`         | Lifecycle modules (comma-separated, e.g., `A1,A2,B6`)      |

Extra columns (e.g., `Uncertainty`, `Comments`) will be ignored.

---

## Quickstart

```bash
python simapro_importer.py \
  --source path/to/raw_lci.csv \
  --modules A1,A2,A3 \
  --destination path/to/simapro_import.csv
```

- `--source`: Path to your raw CSV file.
- `--modules`: Comma-delimited list of modules to include.
- `--destination`: Path to write the formatted import.

---

## Example Workflow

Given **raw_lci.csv**:

| Amount | Unit | Activity                     | Category | Stages |
|--------|------|------------------------------|----------|--------|
| 10.0   | kg   | Steel, low-alloyed [GLO]     | Raw      | A1,A2  |
| 0.005  | kg   | Paint application [IND]      | Air      | A3     |

Run:

```bash
python simapro_importer.py --source raw_lci.csv --modules A1,A2,A3 --destination import.csv
```

Output **import.csv** is ready for SimaPro's Import function.

---

## Development & Testing

1. Clone this repository.
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run unit tests:
   ```bash
   pytest tests/
   ```

---

## Contributing

Contributions are welcome! Please fork the repo, create a feature branch (`git checkout -b feature-name`), commit your changes, and open a pull request.

---

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

Author: Sagar Siripuram (sagar.siripuram95@outlook.com)

Repository: https://github.com/saga9596

