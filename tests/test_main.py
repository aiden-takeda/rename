from collections.abc import Callable, Iterator
from typing import Any

import main as main_module


class StubFile:
    renamed_paths: list[str] = []

    def __init__(self, initial_path: str) -> None:
        self.initial_path = initial_path

    def old_file_name(self) -> str:
        return self.initial_path.rsplit("\\", 1)[-1]

    def new_file_name(self) -> str:
        return self.old_file_name().lower().replace(" ", "-")

    def new_path(self) -> str:
        directory = self.initial_path.rsplit("\\", 1)[0]
        return rf"{directory}\{self.new_file_name()}"

    def rename(self) -> None:
        self.renamed_paths.append(self.initial_path)


def configure_main(
    monkeypatch: Any,
    answers: list[str],
    file_names: list[str],
) -> Callable[[], None]:
    StubFile.renamed_paths = []
    answers_iterator: Iterator[str] = iter(answers)

    monkeypatch.setattr(main_module, "File", StubFile)
    monkeypatch.setattr(main_module.os.path, "isdir", lambda path: True)
    monkeypatch.setattr(
        main_module.os,
        "walk",
        lambda directory: [(directory, [], file_names)],
    )
    monkeypatch.setattr(
        main_module.subprocess,
        "run",
        lambda command, check: None,
    )
    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(answers_iterator),
    )

    return main_module.main


def test_main_noninteractive_renames_changed_files_and_prints_totals(
    monkeypatch: Any, capsys: Any
) -> None:
    run_main = configure_main(
        monkeypatch,
        ["n", r"C:\files"],
        ["My File.txt", "already-normal.txt"],
    )

    run_main()

    assert StubFile.renamed_paths == [r"C:\files\My File.txt"]
    output = capsys.readouterr().out
    assert "Total files: 2" in output
    assert "Renamed files: 1" in output


def test_main_interactive_renames_when_confirmed(monkeypatch: Any, capsys: Any) -> None:
    run_main = configure_main(
        monkeypatch,
        ["y", r"C:\files", "y"],
        ["My File.txt"],
    )

    run_main()

    output = capsys.readouterr().out
    assert StubFile.renamed_paths == [r"C:\files\My File.txt"]
    assert "Old NAME:   My File.txt" in output
    assert "New NAME:   my-file.txt" in output
    assert "Renamed files: 1" in output


def test_main_quit_stops_before_renaming(monkeypatch: Any, capsys: Any) -> None:
    run_main = configure_main(
        monkeypatch,
        ["y", r"C:\files", "q"],
        ["My File.txt", "Another File.txt"],
    )

    run_main()

    assert StubFile.renamed_paths == []
    output = capsys.readouterr().out
    assert "Total files: 1" in output
    assert "Renamed files: 0" in output
    assert "Skipped files: 0" in output
