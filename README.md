# Rename

A small Python utility that renames files in a directory by normalizing the filename to lowercase and converting spaces and punctuation into hyphens while preserving the original folder structure.

## What it does

The tool scans a chosen directory recursively, checks each file name, and renames files when the normalized name differs from the original.

Examples:

- `My File.txt` -> `my-file.txt`
- `notes, draft + copy.txt` -> `notes-draft-copy.txt`
- `chapter. one.txt` -> `chapter-one.txt`

It keeps the original folder layout intact and skips files whose destination name would collide with an existing file.

## How to run

From the project root:

```bash
uv run main.py
```

## How to test

From the project root:

```bash
uv run pytest
```

## Interactive behavior

When you run the script, it will prompt you for:

1. Whether to confirm each rename before applying it.
2. The directory to scan.

If you answer `Y` or press Enter, the script shows the old and new filename and asks whether to rename the file. You can also quit early with `q`.

If you answer `n`, the script does the renames automatically without prompting for each file.

## Notes

- File names are normalized to lowercase.
- Spaces, punctuation, and repeated separators are converted into a single hyphen.
- The extension is preserved.
- The tool does not rename files that already match the normalized output.
- If the destination file already exists, it is skipped to avoid overwriting data.

## Requirements

- Python 3.14+
- No external dependencies
