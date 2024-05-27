from key_pair import generate_keys
from signature import sign_file, verify_file

def main():
    key_pair = generate_keys()
    file_path = "main.py"

    # Генерация подписи файла
    signature = sign_file(file_path, key_pair)
    print(f"Signature: {signature}")

    # Проверка подписи файла
    is_valid = verify_file(file_path, signature, key_pair)
    print(f"Signature valid: {is_valid}")

if __name__ == "__main__":
    main()
