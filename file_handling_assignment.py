def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Hello, World!\n")
            file.write("This is line 2 with a number: 123\n")
            file.write("Line 3 with a float: 45.67\n")
        print("File created successfully.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File creation operation completed.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File contents:")
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File reading operation completed.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appended line 4\n")
            file.write("Appended line 5 with a number: 890\n")
            file.write("Appended line 6 with a float: 12.34\n")
        print("Content appended successfully.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File appending operation completed.")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()

if __name__ == "__main__":
   main()