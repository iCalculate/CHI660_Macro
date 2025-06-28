# CHI660_Macro

[English](README_en.md) | [中文](README_zh.md)

`CHI660_Macro` is a Python toolkit for automatically generating CHI660e workstation macro scripts. It simplifies batch tests such as repeated cycles and parameter sweeps. This guide briefly introduces the macro commands and how to generate them.

## 1. Introduction to CHI workstation macros
Open the macro window from `Control -> Macro Command`. Like Windows batch files or Linux shell scripts, a macro executes a series of commands and is more flexible than simple *Repetitive Runs*.

### Common operations
- **Save**: Save the current macro script to a file. A dialog box will ask for a file name.
- **Run Macro**: Execute the commands in the editor after verifying parameter ranges.
- **Macro Command Editor**: Each line is a command (case-insensitive). Use `:` or `=` to separate a command from its parameter.

![CHI-macro-window](https://pic2.zhimg.com/v2-21baf99afe18cdac6c59cf977294a9ce_r.jpg?source=1940ef5c)

## 2. CHI660e_Macro script generator
The repository provides a `CHI660e` class that generates control scripts with just a few functions. It outputs an editable `TXT` file and an `MCR` file that can be loaded directly into the software.

### Quick start
The following example generates a series of cyclic voltammetry macros:

```python
file = open('output.txt', 'w+')  # create a read‑write text file
chi = CHI660e()                  # initialize the class
chi.init_output_txt(file)        # write header information
scan_rates = (0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5)
for rate in scan_rates:
    chi.init_cv_tech(ei=-0.15, eh=-0.25, el=-0.15, v=rate)
    chi.run_cv(file, f'CV-{rate}', add_note=True)
chi.gene_mcr_file(file)          # build the MCR file
```

The resulting `output.txt` and `output.mcr` can be loaded in CHI software for long-term automated experiments.
