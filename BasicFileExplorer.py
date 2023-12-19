import os


def list_files(path="."):
    print("Listing files in:", path)
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Directory not found.")


def navigate():
    while True:
        path = input("Enter directory path (or 'exit' to quit): ")

        if path.lower() == 'exit':
            break

        list_files(path)


if __name__ == "__main__":
    print("Simple File Explorer in Python")
    navigate()
