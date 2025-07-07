#!/usr/bin/env python3
"""
simapro_importer.py

Convert raw LCI CSV data into a SimaPro-compatible import CSV.

Usage:
    python simapro_importer.py --source path/to/raw_lci.csv \
                               --modules A1,A2,A3 \
                               --destination path/to/import.csv
"""

import argparse
import pandas as pd
import sys

def parse_args():
    parser = argparse.ArgumentParser(
        description='Convert raw LCI CSV to SimaPro import format.'
    )
    parser.add_argument(
        '--source', '-s',
        required=True,
        help='Path to the raw LCI CSV file.'
    )
    parser.add_argument(
        '--modules', '-m',
        help='Comma-separated lifecycle modules to include (e.g. A1,A2). '
             'If omitted, all modules from the input will be included.'
    )
    parser.add_argument(
        '--destination', '-d',
        required=True,
        help='Path to write the SimaPro import CSV.'
    )
    return parser.parse_args()

def main():
    args = parse_args()

    try:
        df = pd.read_csv(args.source)
    except Exception as e:
        print(f"Error reading source file: {e}", file=sys.stderr)
        sys.exit(1)

    # Check required columns
    required_cols = ['Amount', 'Unit', 'Activity', 'Category', 'Stages']
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        print(f"Missing required column(s): {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    # Prepare module filter
    module_filter = None
    if args.modules:
        module_filter = [m.strip() for m in args.modules.split(',') if m.strip()]

    rows = []
    for _, row in df.iterrows():
        # Split stages and strip whitespace
        stages = [m.strip() for m in str(row['Stages']).split(',')]
        for stage in stages:
            if module_filter and stage not in module_filter:
                continue
            rows.append({
                'Flow amount': row['Amount'],
                'Unit': row['Unit'],
                'Simapro name': row['Activity'],
                'Simapro type': row['Category'],
                'Module': stage
            })

    if not rows:
        print("No records matched the module filter.", file=sys.stderr)
        sys.exit(1)

    out_df = pd.DataFrame(rows, columns=[
        'Flow amount',
        'Unit',
        'Simapro name',
        'Simapro type',
        'Module'
    ])

    try:
        out_df.to_csv(args.destination, index=False)
        print(f"Exported {len(out_df)} rows to {args.destination}")
    except Exception as e:
        print(f"Error writing destination file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
