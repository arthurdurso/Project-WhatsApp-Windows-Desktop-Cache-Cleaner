import os


def remove_files_in_directory(directory_path):
    try:
        # List all files in the directory
        files = os.listdir(directory_path)
        
        # Iterate over the list of files and remove each one
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Removed file: {file_path}")
            elif os.path.isdir(file_path):
                print(f"Skipped directory: {file_path}")
                
    except Exception as e:
        print(f"Error: {e}")


# Usage
directory_path = r'C:\Users\Durso\AppData\Local\Packages\5319275A.WhatsAppDesktop_cv1g1gvanyjgm\LocalState\shared\transfers'
remove_files_in_directory(directory_path)
