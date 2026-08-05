import os
import subprocess

def main():
    command = ["cmd", "/c", "cls"]
    subprocess.run(command)
    total_files = 0
    renamed_files = 0

    ask_for = True
    answer = input("Do you want to confirm each rename? (Y/n): ")
    if answer.lower() == 'n':
        ask_for = False

    dir = str(input("Directory: "))

    paths = (os.path.join(root, file_namename)
            for root, _, file_namenames in os.walk(dir)
            for file_namename in file_namenames)

    for path in paths:
        total_files +=1
        old_path = path
        file_name = old_path.split('\\')[-1]
        path = '\\'.join(old_path.split('\\')[:-1])
        
        file_name = file_name.lower()
        file_name = file_name.replace('. ', '-')
        file_name = file_name.replace(' ', '-')
        
        new_path = path + '\\'+file_name
        
        if old_path != new_path:
            if ask_for:
                print('-' * 100)
                print(old_path)
                print(new_path)
                curr_rename = input("Rename this file (Y/n): ")

                if curr_rename.lower() == 'y':
                    renamed_files += 1
                    os.rename(old_path, new_path)
                    
            else:
                renamed_files += 1
                os.rename(old_path, new_path)


    print("=" * 100)
    print(f"Total files: {total_files}")
    print(f"Renamed files: {renamed_files}")

if __name__ == "__main__":
    main()