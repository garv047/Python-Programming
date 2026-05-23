# 5.	Create multiple suitable exceptions for a file handling program.

class FileEmptyError(Exception):
    pass

class InvalidFileExtensionError(Exception):
    pass

class DataFormatError(Exception):
    pass

def process_file(filename):
    try:
        if not filename.endswith(".txt"):
            raise InvalidFileExtensionError("Only .txt files are allowed.")

        with open(filename, "r") as f:
            content = f.read()

            if not content.strip():
                raise FileEmptyError("The file is empty.")

            lines = content.splitlines()
            for line in lines:
                if not line.replace(" ", "").isalnum():
                    raise DataFormatError(f"Invalid characters found in line: {line}")

            print("File processed successfully.")

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except PermissionError:
        print("Error: You do not have permission to access this file.")
    except InvalidFileExtensionError as e:
        print(f"Extension Error: {e}")
    except FileEmptyError as e:
        print(f"Content Error: {e}")
    except DataFormatError as e:
        print(f"Format Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

process_file("data.txt")
