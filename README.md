# Clean WhatsApp Desktop Cache for Windows

## Project Overview

This is my first solo project where I am developing a script to clean the WhatsApp cache. The primary goal is to improve the application's performance and execution speed by identifying and removing unnecessary cache data without affecting important user conversations or data.

## Features

- **Cache Cleaning**: The script safely identifies and removes unnecessary cache data.
- **Performance Improvement**: Clearing the cache will significantly enhance WhatsApp's performance.

## Implementation

The script is written in Python, utilizing the `os` and `shutil` libraries to handle file and directory operations. Initially, the script is configured to run with my user as the default, but future commits will ensure it can be used by anyone.

### Script Details

- **Libraries Used**:
  - `os`
  - `shutil`
  
- **Functionality**:
  - Verifies every file and subdirectory in the specified directory path.
  - Safely removes unnecessary cache files.

## Creating an Executable

An executable was created from the Python script using PyInstaller, to run on the startup folder. To recreate the executable, follow these steps: (Don't need to install pyinstaller, because it's already installed on the .venv)

1. **Generate the Executable**: Run the following command in your terminal or Git Bash to create a single executable file:

pyinstaller --onefile main.py

Locate the Executable: After PyInstaller completes, find the executable in the dist folder within your project directory.

Clean Up: Remove the build, dist, and main.spec files from your project directory, because you will only need the executable.


## Scheduling Options

There are two ways that could be scheduled the cache cleaning task:

### Execute on Startup (Recommended)

- **Description**: The script runs every time the PC logs in, ensuring optimal performance by clearing the cache regularly.
- **Advantages**: Consistent performance improvement; no dependency on specific times or the system being turned on.

### Task Scheduler (Windows)

- **Description**: A traditional method to schedule tasks on Windows.
- **Advantages**: Simple and well-known method.
- **Disadvantages**: May not run if the PC is turned off at the scheduled time.

## Conclusion

The best approach is to execute the script on startup, ensuring the cache is cleared every time the PC logs in for the best performance. While Task Scheduler is a valid options, but it has limitations that make it less ideal for this project.


## Adding the Executable to Startup

To ensure the executable runs automatically when the PC starts, follow these steps:

1. **Open the Startup Folder**: Navigate to the Startup folder:
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup

2. Move the created shortcut to the Startup folder.

By doing this, the script will run each time the computer logs in, ensuring that the cache is regularly cleaned.