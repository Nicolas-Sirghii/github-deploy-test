from pathlib import Path

file = Path("test.txt")

assert file.exists(), "test.txt does not exist!"

content = file.read_text()

assert content == "Hello GitHub! it worked again!", "Incorrect file content!"

print("All tests passed!")