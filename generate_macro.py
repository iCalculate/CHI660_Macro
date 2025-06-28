#!/usr/bin/env python3
"""Command line tool to generate CHI660E macro scripts from a JSON config."""
import argparse
import json
from chi_macro import CHI660e


def main():
    parser = argparse.ArgumentParser(description="Generate CHI660E macro from JSON config")
    parser.add_argument('--config', required=True, help='JSON configuration file')
    parser.add_argument('--output', default='output.txt', help='Output macro text file')
    args = parser.parse_args()

    with open(args.config) as f:
        cfg = json.load(f)

    with open(args.output, 'w+') as out:
        chi = CHI660e()
        chi.init_output_txt(out)

        for step in cfg.get('steps', []):
            cmd = step.get('command')
            params = step.get('params', {})
            fname = step.get('filename', cmd)
            if cmd == 'beep':
                chi.beep(out, params.get('times', 1), params.get('interval', 1))
            elif cmd == 'cv':
                chi.init_cv_tech(**params)
                chi.run_cv(out, fname, add_note=True)
            elif cmd == 'lsv':
                chi.init_lsv_tech(**params)
                chi.run_lsv(out, fname, add_note=True)
            elif cmd == 'scv':
                chi.init_scv_tech(**params)
                chi.run_scv(out, fname, add_note=True)
            elif cmd == 'it':
                chi.init_it_tech(**params)
                chi.run_it(out, fname, add_note=True)
            elif cmd == 'be':
                chi.init_be_tech(**params)
                chi.run_be(out, fname, add_note=True)
            elif cmd == 'imp':
                chi.init_imp_tech(**params)
                chi.run_imp(out, fname, add_note=True)
            else:
                print(f"Unknown command: {cmd}")

        chi.gene_mcr_file(out)


if __name__ == '__main__':
    main()
