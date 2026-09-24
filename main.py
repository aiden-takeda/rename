import os
import subprocess

from my_file.file import File

COMMAND: list[str] = ["cmd", "/c", "cls"]


def output(total: int, renamed: int, skipped: int) -> None:
    print("=" * 100)
    print(f"Total files: {total}")
    print(f"Renamed files: {renamed}")
    print(f"Skipped files: {skipped}")


def main() -> None:
    # Clear the screen when started
    if os.name == "nt":
        subprocess.run(COMMAND, check=False)
    else:
        subprocess.run(["clear"], check=False)

    # Variables to keep the values of total files and renamed files.
    total_files: int = 0
    renamed_files: int = 0
    skipped_files: int = 0

    # Ask the user whether to confirm each renaming before proceeding.
    is_interactive: bool = True
    answer: str = (
        input("Confirm each rename before applying it? [Y/n]: ").strip().lower()
    )
    if answer in {"n", "no"}:
        is_interactive = False
    elif answer not in {"", "y", "yes"}:
        print("Using the default: confirm each rename.")

    # Request for user where files are located
    directory: str = input("Directory to scan: ").strip()
    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        return

    # List of all paths
    paths = (
        os.path.join(root, file_name)
        for root, _, file_names in os.walk(directory)
        for file_name in file_names
    )

    for path in paths:
        total_files += 1
        curr_file: File = File(path)
        new_path: str = curr_file.new_path()

        if path != new_path:
            if is_interactive:
                print("-" * 100)
                print(f"Old NAME:   {curr_file.old_file_name()}")
                print(f"New NAME:   {curr_file.new_file_name()}")
                ask_for_curr_rename: str = (
                    input("Rename this file? [Y/n/q]: ").strip().lower()
                )

                if ask_for_curr_rename == "q":
                    output(total_files, renamed_files, skipped_files)
                    return

                if ask_for_curr_rename in {"", "y", "yes"}:
                    renamed_files += 1
                    try:
                        curr_file.rename()
                    except FileExistsError:
                        print(
                            f"Skipping {curr_file.old_file_name()}: destination already exists."
                        )
                        renamed_files -= 1
                        skipped_files += 1

            else:
                renamed_files += 1
                try:
                    curr_file.rename()
                except FileExistsError:
                    print(
                        f"Skipping {curr_file.old_file_name()}: destination already exists."
                    )
                    renamed_files -= 1
                    skipped_files += 1

    output(total_files, renamed_files, skipped_files)


if __name__ == "__main__":
    main()
