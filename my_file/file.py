import os
import re


class File:
    """Represent a file and the normalized name it should be renamed to."""

    def __init__(self, initial_path: str) -> None:
        """Store the file's current path."""
        self.initial_path: str = initial_path

    def old_file_name(self) -> str:
        """Return the file name extracted from the current path."""
        normalized_path: str = self.initial_path.replace("\\", "/")
        return normalized_path.rsplit("/", 1)[-1]

    def new_file_name(self) -> str:
        """Return a lowercase, separator-normalized version of the file name."""
        file_name: str = self.old_file_name()
        base_name, extension = os.path.splitext(file_name.lower())
        sanitized_name: str = re.sub(r"[^a-z0-9()]+", "-", base_name)
        sanitized_name = re.sub(r"(?<=[a-z0-9])\(", "-(", sanitized_name)
        sanitized_name = re.sub(r"\)(?=[a-z0-9])", ")-", sanitized_name)
        sanitized_name = re.sub(r"-{2,}", "-", sanitized_name)
        sanitized_name = sanitized_name.strip("-")

        if not sanitized_name:
            sanitized_name = "untitled"

        return f"{sanitized_name}{extension.lower()}"

    def new_path(self) -> str:
        """Return the path that combines the original directory and new name."""
        directory: str = os.path.dirname(self.initial_path)
        return os.path.join(directory, self.new_file_name())

    def rename(self) -> None:
        """Rename the file on disk to its normalized path."""
        new_path = self.new_path()

        if os.path.abspath(new_path) == os.path.abspath(self.initial_path):
            return

        if os.path.exists(new_path):
            raise FileExistsError(f"Destination already exists: {new_path}")

        os.rename(self.initial_path, new_path)
