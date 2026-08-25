import os
import shutil


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) < 3 or parts[0] != "mv":
        raise ValueError("Invalid command format")

    src = parts[1]
    dest = parts[2]

    # If destination ends with '/', treat it as a directory
    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(src))

    # Ensure destination directory exists
    dest_dir = os.path.dirname(dest)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    # Copy file content to destination
    shutil.copy2(src, dest)

    # Remove the source file
    os.remove(src)
