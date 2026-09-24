from pathlib import Path

import pytest

from my_file.file import File


def test_old_file_name_returns_name_from_path() -> None:
    file = File(r"C:\Users\Anton\My File.txt")

    assert file.old_file_name() == "My File.txt"


@pytest.mark.parametrize(
    ("initial_name", "expected_name"),
    [
        ("Report FINAL.TXT", "report-final.txt"),
        ("notes, draft + copy.txt", "notes-draft-copy.txt"),
        ("chapter. one.txt", "chapter-one.txt"),
        ("many    spaces.txt", "many-spaces.txt"),
        ("file__name!!!.txt", "file-name.txt"),
        ("copilot-instructions(26).md", "copilot-instructions-(26).md"),
    ],
)
def test_new_file_name_normalizes_name(initial_name: str, expected_name: str) -> None:
    file = File(rf"C:\Users\Anton\{initial_name}")

    assert file.new_file_name() == expected_name


def test_new_path_preserves_directory() -> None:
    file = File(r"C:\Users\Anton\My File.txt")

    assert file.new_path() == r"C:\Users\Anton\my-file.txt"


def test_rename_renames_file_on_disk(tmp_path: Path) -> None:
    original_path = tmp_path / "My File.txt"
    original_path.write_text("content", encoding="utf-8")
    file = File(str(original_path))

    file.rename()

    renamed_path = tmp_path / "my-file.txt"
    assert not original_path.exists()
    assert renamed_path.read_text(encoding="utf-8") == "content"


def test_rename_raises_when_destination_already_exists(tmp_path: Path) -> None:
    original_path = tmp_path / "My File.txt"
    original_path.write_text("content", encoding="utf-8")
    destination_path = tmp_path / "my-file.txt"
    destination_path.write_text("existing", encoding="utf-8")

    file = File(str(original_path))

    with pytest.raises(FileExistsError):
        file.rename()
