import os

class File:
    def __init__(self, initinal_path: str) -> None:
        self.initinal_path:str = initinal_path

    def old_file_name(self) -> str:
        file_name: str = self.initinal_path.split('\\')[-1]

        return file_name

    def new_file_name(self) -> str:
        file_name: str = self.initinal_path.split('\\')[-1]
        file_name = file_name.lower()
        file_name = file_name.replace('. ', '-')
        file_name = file_name.replace(' ', '-')
        
        return file_name

    def new_path(self) -> str:
        path: str = '\\'.join(self.initinal_path.split('\\')[:-1])
        path += '\\' + self.new_file_name()
        
        return path

    def rename(self) -> None:
        os.rename(self.initinal_path, self.new_path())