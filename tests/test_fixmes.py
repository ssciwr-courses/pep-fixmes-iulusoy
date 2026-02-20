import subprocess
from pathlib import Path


def test_ruff_check():
    # Get the repository directory
    current_dir = Path(__file__).resolve().parents[1]
    input_file_path = current_dir / "chapter1"
    # run ruff on the example files one by one and check if there are any stylistic errors
    files = [input_file_path / "example1.py", input_file_path / "example2.py", input_file_path / "example3.py"]
    total_failure = 0
    for file in files:
        command = f"ruff check --preview {file}"
        failure = 0
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                failure = 1
        except subprocess.CalledProcessError as e:
            failure = e.returncode
        # if there are some, print the differences and calculate no of errors
        if failure == 1:
            print(result.stdout)
            print(f"Please try again for file {file}!")
        elif failure == 0:
            print(f"No stylistic errors found for file {file}!")
        else:
            print("An error occurred while running ruff!")
        total_failure += failure
    assert total_failure == 0


def test_german_name():
    # Kreis in example 2
    current_dir = Path(__file__).resolve().parents[1]
    input_file = current_dir / "chapter1" / "example2.py"
    # figure out if the word "Kreis" is in the file
    with open(input_file, "r") as f:
        file_content = f.read()
    assert "Kreis" not in file_content

