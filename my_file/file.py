import os


class File:
    """Represent a file and the normalized name it should be renamed to."""

    def __init__(self, initial_path: str) -> None:
        """Store the file's current path."""
        self.initial_path: str = initial_path

    def old_file_name(self) -> str:
        """Return the file name extracted from the current path."""
        file_name: str = os.path.basename(self.initial_path)

        if file_name == self.initial_path and "\\" in self.initial_path:
            file_name = self.initial_path.rsplit("\\", 1)[-1]

        return file_name

    def new_file_name(self) -> str:
        """Return a lowercase, separator-normalized version of the file name."""
        file_name: str = self.old_file_name()
        file_name = file_name.lower()
        file_name = file_name.replace(", ", " ")
        file_name = file_name.replace(". ", "-")
        file_name = file_name.replace(" ", "-")
        file_name = file_name.replace("+", "-")
        file_name = file_name.replace("----", "---")

        return file_name

    def new_path(self) -> str:
        """Return the path that combines the original directory and new name."""
        directory: str = os.path.dirname(self.initial_path)
        if "\\" in self.initial_path and os.sep != "\\":
            return directory + "\\" + self.new_file_name()

        path: str = os.path.join(directory, self.new_file_name())

        return path

    def rename(self) -> None:
        """Rename the file on disk to its normalized path."""
        os.rename(self.initial_path, self.new_path())
