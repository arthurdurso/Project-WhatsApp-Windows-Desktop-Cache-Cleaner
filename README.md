# Clean WhatsApp Desktop Windows Cache

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



## To write:

- user pyinstaller "pyinstaller --onefile main.py" to get just one file exe. get the file on the folder 'dist' and remove the 'build and 'dist' and 'main.spec'.
- Need to do a step by step to put the exe file in the startup folder. the folder: C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup