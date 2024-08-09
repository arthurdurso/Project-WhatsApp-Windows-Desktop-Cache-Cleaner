import os               # OS operations and file paths
import shutil           # File and directory management


def find_whatsapp_directory(base_path):
    try:
        # List all directories in the base path
        directories = os.listdir(base_path)
        
        # Search for a directory containing "WhatsAppDesktop" in its name
        for directory in directories:
            if "WhatsAppDesktop" in directory:
                full_path = os.path.join(base_path, directory)
                return full_path
            
    except Exception as e:
        # Handle exceptions silently
        pass
    return None


def remove_all_files_in_directory(directory_path):
    try:
        # List all files in the directory
        files = os.listdir(directory_path)
        
        # Iterate over the list of files and remove each one
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                
    except Exception as e:
        # Handle exceptions silently
        pass


def main():

    # Define the base path where WhatsApp packages are stored
    user_profile = os.environ['USERPROFILE']
    base_path = os.path.join(user_profile, r'AppData\Local\Packages')
    whatsapp_directory = find_whatsapp_directory(base_path)
    
    # Remove all files and directories within the 'transfers' directory
    directory_path = os.path.join(whatsapp_directory, r'LocalState\shared\transfers')
    remove_all_files_in_directory(directory_path)


if __name__ == "__main__":
    main()
