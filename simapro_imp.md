[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![python](https://img.shields.io/badge/python-3.7%2B-green.svg)]()

# Simapro LCI Import Converter
Python utility to convert LCI CSV data into SimaPro-compatible import files.

A lightweight Python utility that streamlines Life Cycle Inventory (LCI) data ingestion into SimaPro. Simply feed it your raw CSV exports, specify your modules, and it produces a formatted import file—no manual tweaks required.

## Table of Contents

- [Key Highlights](#key-highlights)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Input Specification](#input-specification)
- [Quickstart](#quickstart)
- [Example Workflow](#example-workflow)
- [Getting Started (For Non-Programmers)](#getting-started-for-non-programmers)
- [Troubleshooting](#troubleshooting)
- [Development & Testing](#development--testing)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)
- [Contact](#contact)

---

## Key Highlights

- **Effortless Transformation**: Convert raw LCI tables (CSV) directly into SimaPro-compatible imports.  
- **Module Selection**: Choose any combination of lifecycle stages (e.g., A1–A4, B6).  
- **Automated Mapping**: Smart detection of flow names, units, and categories.  
- **Clean Output**: Drops unsupported fields (uncertainty, comments) and retains only what SimaPro needs.

---

## Prerequisites

- **Python 3.7 or above**  
- [pandas](https://pandas.pydata.org/)  
- [numpy](https://numpy.org/)

---

## Installation

Install the necessary libraries:

```bash
pip install pandas numpy
# Or, once published to PyPI:
pip install simapro-lci-importer
```

---

## Input Specification

Your input CSV must include these columns:

| Column    | Description                                            |
|-----------|--------------------------------------------------------|
| `Amount`  | Numeric value of the flow                              |
| `Unit`    | Unit (e.g., `kg`, `m³`, `MJ`)                         |
| `Activity`| Exact SimaPro dataset or process name (case sensitive) |
| `Category`| Flow category (e.g., `Raw`, `Air`, `Water`, `Waste`)   |
| `Stages`  | Lifecycle modules (comma-separated, e.g., `A1,A2,B6`)  |

Any extra columns (e.g., `Uncertainty`, `Comments`) are ignored.

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

Output **import.csv** is ready for SimaPro’s Import function.

---

## Getting Started (For Non-Programmers)

1. **Install Python**  
   - Download from: https://www.python.org/downloads/  
   - During installation, check “Add Python to PATH.”

2. **Download the tool**  
   - Visit: https://github.com/Saga9596/simapro-csv-importer  
   - Click **Code ▶ Download ZIP**, then unzip to a folder.

3. **Open Terminal / Command Prompt**  
   - **Windows**: Win+R → `cmd` → Enter  
   - **Mac**: Applications ▶ Utilities ▶ Terminal

4. **Navigate to the folder**  
```bash
cd path/to/simapro-csv-importer
```

5. **Install dependencies**  
```bash
pip install pandas numpy
```

6. **Prepare your CSV**  
Ensure it matches the **Input Specification** above.

7. **Run the converter**  
```bash
python simapro_importer.py --source raw_lci.csv --modules A1,A2 --destination import.csv
```

8. **Import into SimaPro**  
Open SimaPro and use **Import** to load `import.csv`.

---

## Troubleshooting

- **Missing required column(s)**: Ensure your CSV has `Amount`, `Unit`, `Activity`, `Category`, and `Stages`.  
- **No records matched the module filter**: Check that modules passed to `--modules` match entries in `Stages`.  
- **Command not found**: Verify Python is installed and added to your PATH.

---

## Development & Testing

1. Clone the repository.  
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run tests:
```bash
pytest tests/
```

---

## Contributing

Contributions are welcome! Fork the repo, create a feature branch, commit changes, and open a pull request.  
Please read our [Code of Conduct](CODE_OF_CONDUCT.md) first.

---

## Roadmap

Upcoming features and improvements:

- **Bulk import of multiple CSVs**: Support processing multiple LCI files in a single command.  
- **Custom column mappings**: Allow users to map arbitrary CSV column names to SimaPro import fields via a config file.  
- **Graphical User Interface (GUI)**: Develop a simple desktop or web UI for users unfamiliar with the command line.  
- **Publish on PyPI**: Package and distribute the tool via pip for easier installation.  
- **Enhanced logging and verbose mode**: Add detailed logs and a `--verbose` flag for troubleshooting.  
- **Automated testing and CI**: Integrate GitHub Actions to run tests on every pull request.

---

## License

MIT License. See [LICENSE](LICENSE).

---

## Contact

**Author:** Sagar Siripuram  
**Email:** sagar.siripuram95@outlook.com  
**Repo:** https://github.com/Saga9596/simapro-csv-importer
