
# Combined solution for File Read & Write Challenge 🖋️ and Error Handling Lab 🧪

def file_read_write_challenge():
    """Reads input.txt, modifies content, and writes to output.txt"""
    try:
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Modify content (example: convert text to uppercase)
        modified_content = content.upper()

        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File has been read, modified, and saved as 'output.txt'")

    except FileNotFoundError:
        print("❌ Error: 'input.txt' was not found. Please make sure the file exists.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


def error_handling_lab():
    """Asks the user for a filename and handles errors gracefully"""
    try:
        filename = input("\n📂 Enter the filename to read: ")
        with open(filename, "r") as file:
            content = file.read()
            print("\n📄 File Content:\n")
            print(content)

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
    finally:
        print("🔒 File handling operation completed.")


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    print("=== File Handling & Exception Handling Assignment ===\n")

    # Run File Read & Write Challenge
    file_read_write_challenge()

    # Run Error Handling Lab
    error_handling_lab()

