# Step 1–3: Open, read, and print file content with error handling
try:
    file1 = open("sample.txt","r")
    reading_line = file1.readline(2)
    print(reading_line)
    file1.close()
    print("reading file content")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

