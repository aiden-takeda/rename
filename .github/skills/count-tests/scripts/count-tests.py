import io
import json
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Any

import pytest


class TestCollector:
    def __init__(self) -> None:
        self.total_tests = 0

    def pytest_collection_finish(self, session: Any) -> None:
        self.total_tests = len(session.items)


def count_tests(project_root: Path | None = None) -> dict[str, int]:
    if project_root is None:
        project_root = Path(__file__).resolve().parents[4]

    tests_directory = project_root / "tests"
    test_files = {
        *tests_directory.rglob("test_*.py"),
        *tests_directory.rglob("*_test.py"),
    }
    collector = TestCollector()

    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
        exit_code = pytest.main(
            ["--collect-only", "-q", str(tests_directory)],
            plugins=[collector],
        )

    if exit_code not in (pytest.ExitCode.OK, pytest.ExitCode.NO_TESTS_COLLECTED):
        raise RuntimeError(f"pytest collection failed with exit code {exit_code}")

    total_files = len(test_files)
    total_tests = collector.total_tests

    return {"total_files": total_files, "total_tests": total_tests}


if __name__ == "__main__":
    print(json.dumps(count_tests()))
