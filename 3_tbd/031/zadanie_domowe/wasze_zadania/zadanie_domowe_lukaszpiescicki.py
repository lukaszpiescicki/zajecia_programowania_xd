from secure_data_hasher import encrypt_file
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        encrypt_file(file_path)
