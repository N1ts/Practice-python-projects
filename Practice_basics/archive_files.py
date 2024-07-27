import shutil

files = shutil.make_archive("archived_files", "zip", "files_to_fetch")

print(files)