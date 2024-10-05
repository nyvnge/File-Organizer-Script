import os
import shutil
from pathlib import Path

def create_folder(directory):
    """Create folder if it doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def organize_files(source_dir):
    # Dictionary mapping file extensions to their respective folders
    extension_mapping = {
        # Audio/Music files
        '.mp3': 'Music/Audio',
        '.wav': 'Music/Audio',
        '.flac': 'Music/Audio',
        '.m4a': 'Music/Audio',
        
        # Video files
        '.mp4': 'Videos',
        '.mov': 'Videos',
        '.avi': 'Videos',
        '.mkv': 'Videos',
        
        # Image files
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        
        # Documents
        '.pdf': 'Documents',
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.txt': 'Documents',
        '.rtf': 'Documents',
        
        # Spreadsheets
        '.xlsx': 'Spreadsheets',
        '.xls': 'Spreadsheets',
        '.csv': 'Spreadsheets',
        
        # Presentations
        '.ppt': 'Presentations',
        '.pptx': 'Presentations',
        
        # Archives
        '.zip': 'Archives',
        '.rar': 'Archives',
        '.7z': 'Archives',
        
        # Programming files
        '.py': 'Code',
        '.java': 'Code',
        '.cpp': 'Code',
        '.html': 'Code',
        '.css': 'Code',
        '.js': 'Code'
    }
    
    # Convert source_dir to Path object
    source_path = Path(source_dir)
    
    # Counter for moved files
    moved_files = 0
    
    print(f"Scanning directory: {source_dir}")
    
    # Iterate through all files in the source directory
    for file_path in source_path.glob('*'):
        # Skip if it's a directory
        if file_path.is_dir():
            continue
            
        # Get the file extension
        file_extension = file_path.suffix.lower()
        
        # Skip if no extension
        if not file_extension:
            continue
            
        # Get the destination folder based on extension
        dest_folder = extension_mapping.get(file_extension, 'Others')
        
        # Create full destination path
        dest_path = source_path / dest_folder
        
        # Create destination folder if it doesn't exist
        create_folder(dest_path)
        
        try:
            # Check if destination file already exists
            dest_file = dest_path / file_path.name
            if dest_file.exists():
                # Add number to filename if it already exists
                base_name = dest_file.stem
                extension = dest_file.suffix
                counter = 1
                while dest_file.exists():
                    new_name = f"{base_name}_{counter}{extension}"
                    dest_file = dest_path / new_name
                    counter += 1
            
            # Move the file
            shutil.move(str(file_path), str(dest_file))
            moved_files += 1
            print(f"Moved: {file_path.name} -> {dest_folder}/")
        except Exception as e:
            print(f"Error moving {file_path.name}: {str(e)}")
    
    return moved_files

def main():
    # Set the source directory (Downloads folder)
    source_dir = r"C:\Users\Sanderson Nyange\Downloads"
    
    print("Starting file organization...")
    print(f"Organizing files in: {source_dir}")
    
    # Organize the files
    moved_files = organize_files(source_dir)
    
    print(f"\nOrganization complete!")
    print(f"Total files moved: {moved_files}")

if __name__ == "__main__":
    main()