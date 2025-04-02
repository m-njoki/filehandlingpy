def modify_file():
    filename = input("Enter the file name to read from: ")

    try:
        with open(filename, "r") as file:
            data = file.read()

        modified_data = data.upper()  # Modify data to uppercase

        output_filename = "output.txt"
        with open(output_filename, "w") as file:
            file.write(modified_data)

        print(f"File successfully modified and saved as '{output_filename}'.")

        # Display the contents of the modified file
        print("\nContents of the modified file:")
        with open(output_filename, "r") as file:
            print(file.read())

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
modify_file()
