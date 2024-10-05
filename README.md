# File Organizer Script 🗂️

A Python script that automatically organizes files in a specified directory by sorting them into folders based on their file extensions. Perfect for keeping your Downloads folder (or any other directory) neat and organized!

## Features ✨

- Automatically creates folders based on file types
- Handles duplicate filenames
- Provides real-time feedback during organization
- Supports multiple file formats including:
  - Audio/Music files (.mp3, .wav, .flac, .m4a)
  - Video files (.mp4, .mov, .avi, .mkv)
  - Images (.jpg, .jpeg, .png, .gif)
  - Documents (.pdf, .doc, .docx, .txt, .rtf)
  - Spreadsheets (.xlsx, .xls, .csv)
  - Presentations (.ppt, .pptx)
  - Archives (.zip, .rar, .7z)
  - Programming files (.py, .java, .cpp, .html, .css, .js)
  - Others (for unsupported extensions)

## Prerequisites 📋

- Python 3.6 or higher
- Operating System: Windows, macOS, or Linux

## Installation 🔧

1. Clone this repository or download the script:
```bash
git clone [repository-url]
# or download organize_files.py directly
```

2. No additional Python packages are required as the script uses only standard library modules.

## Usage 💻

1. Place the script in a directory of your choice:
```
C:\Users\YourUsername\Downloads\organize\organize_files.py
```

2. Modify the source directory in the script (if needed):
```python
source_dir = r"C:\Users\YourUsername\Downloads"  # Change this to your desired directory
```

3. Run the script:
```bash
python organize_files.py
```

## Directory Structure 📁

After running the script, your files will be organized into the following structure:

```
Source Directory/
├── Music/Audio/
├── Videos/
├── Images/
├── Documents/
├── Spreadsheets/
├── Presentations/
├── Archives/
├── Code/
└── Others/
```

## Screenshots 📸

### Before Organization
[Add your screenshot here showing messy directory]

### After Organization
[Add your screenshot here showing organized directory]

### Script in Action
[Add your screenshot here showing the script running]

## Customization 🛠️

You can customize the script by:

1. Adding new file extensions:
```python
extension_mapping = {
    '.your_extension': 'Your Folder Name',
    # Add more extensions here
}
```

2. Modifying existing folder names:
```python
'.mp3': 'Your Custom Music Folder Name',
```

## Contributing 🤝

1. Fork the repository
2. Create a new branch for your features
3. Submit a pull request

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.
[6~
