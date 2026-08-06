import os
import subprocess

from my_file.file import File

COMMAND: list[str] = ["cmd", "/c", "cls"]

def main():
    # Clear the screen when started
    subprocess.run(COMMAND)

    # Variables to keep the values of total files and renamed files.
    total_files: int = 0
    renamed_files: int = 0

    # Ask user if wants to be asked for each renaming (IMPORT: if files are many it will be annoying)
    is_interactive: bool = True
    answer: str = input("Do you want to confirm each rename? (Y/n): ")
    if answer.lower() == 'n':
        is_interactive = False

    # Request for user where files are located
    dir = str(input("Directory: "))

    # List of all paths 
    paths = (os.path.join(root, file_namename)
            for root, _, file_namenames in os.walk(dir)
            for file_namename in file_namenames)

    for path in paths:
        total_files +=1
        curr_file: File = File(path)
        new_path: str = curr_file.new_path()
        
        if path != new_path:
            if is_interactive:
                print('-' * 100)
                print(f"Old NAME:   {curr_file.old_file_name()}")
                print(f"New NAME:   {curr_file.new_file_name()}")
                ask_for_curr_rename: str = input("Do you want to rename this file (Y/n) or (q) for quit: ")

                if ask_for_curr_rename.lower() == 'q':
                    return

                if ask_for_curr_rename.lower() == 'y':
                    renamed_files += 1
                    curr_file.rename()
                    
            else:
                renamed_files += 1
                curr_file.rename()

    print("=" * 100)
    print(f"Total files: {total_files}")
    print(f"Renamed files: {renamed_files}")

if __name__ == "__main__":
    main()