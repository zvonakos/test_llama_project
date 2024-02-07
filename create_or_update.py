import os


def create_or_update_index(filename: str, content: str):  # I think there are quicker and more efficient way to create file in the library, but I've decided to make my own
    if 'txt' in filename:
        try:
            file_path = os.path.join('data', f'{filename}')
            with open(file_path, 'w') as file:
                file.write(content)
                return True
        except Exception as e:
            print(f"Error occurred while creating/updating file '{file_path}': {e}")
    else:
        return False