# Lab Guide for PVT Lisbon 2026 Lab LAB-31056

Web guide link: https://canewton-ccep.github.io/PTE-Lisbon-Dial-Plan-Lab/


## DOCX to Markdown script

Use `scripts/docx_to_markdown.py` to convert a DOCX lab guide into markdown files.

### What it does

- Reads one `.docx` input file
- Extracts all embedded images into `docs/assets/` (or a custom assets directory)
- Splits each Heading 1/Heading 2 that starts with `Lab` into its own markdown file in `docs/`
- Writes all non-lab content to `docs/non-lab.md`

### Usage

```bash
python scripts/docx_to_markdown.py path/to/guide.docx
```

Optional arguments:

- `--docs-dir` (default: `docs`)
- `--assets-dir` (default: `<docs-dir>/assets`)
