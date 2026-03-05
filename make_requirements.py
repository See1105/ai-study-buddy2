import subprocess

try:
    with open('requirements.txt', 'w', encoding='utf-8') as f:
        output = subprocess.check_output(['pip', 'freeze'], text=True)
        f.write(output)
    print("requirements.txt created successfully.")
except Exception as e:
    print(f"Error: {e}")
