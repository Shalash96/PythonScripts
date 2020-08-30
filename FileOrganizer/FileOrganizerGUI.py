from tkinter import *
import os
import shutil

root = Tk()
root.geometry('400x100')
root.title('File organizer')
Label(root, text='Enter directory').grid(row=0, column=0)
dirPath = Entry(root, width=35)
dirPath.grid(row=0, column=1)
directories = {
        "HTML": (".html5", ".html", ".htm", ".xhtml"),
        "IMAGES": (".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg",
                   "svg", ".heif", ".psd"),
        "VIDEOS": (".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob",
                   ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"),
        "DOCUMENTS": (".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                      ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                      "pptx"),
        "ARCHIVES": (".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"),
        "AUDIO": (".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                  ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"),
        "PLAINTEXT": (".txt", ".in", ".out"),
        "PDF": ".pdf",
        "PYTHON": ".py",
        "EXE": ".exe",
        "OTHER": "",
        "FOLDERS": ""
    }


def create_folders(directories, directory_path):
    for key in directories:
        if key not in os.listdir(directory_path):
            os.mkdir(directory_path + '/' + key)
    if "OTHER" not in os.listdir(directory_path):
        os.mkdir(directory_path + '/' + "OTHER")


def organize_folders(directories, directory_path):
    for file in os.listdir(directory_path):
        if os.path.isfile(directory_path + '/' + file):
            src_path = directory_path + '/' + file
            for key in directories:
                extension = directories[key]
                if file.endswith(extension):
                    dest_path = os.path.join(directory_path, key, file)
                    shutil.move(src_path, dest_path)
                    break


def organize_remaining_files(directory_path):
    for file in os.listdir(directory_path):
        if os.path.isfile(directory_path + '/' + file):
            src_path = directory_path + '/' + file
            dest_path = os.path.join(directory_path, "OTHER", file)
            shutil.move(src_path, dest_path)


def organize_remaining_folders(directories, directory_path):
    list_dir = os.listdir(directory_path)
    organized_folders = []
    for folder in directories:
        organized_folders.append(folder)
    organized_folders = tuple(organized_folders)
    for folder in list_dir:
        if folder not in organized_folders:
            src_path = directory_path + '/' + folder
            dest_path = os.path.join(directory_path, "FOLDERS", folder)
            shutil.move(src_path, dest_path)


def organize(dirPath):
    directory_path = str(dirPath)
    create_folders(directories, directory_path)
    organize_folders(directories, directory_path)
    organize_remaining_files(directory_path)
    organize_remaining_folders(directories, directory_path)


Button(root, text='Organize', command=lambda: organize(dirPath.get())).grid(row=1, column=1)
root.mainloop()
