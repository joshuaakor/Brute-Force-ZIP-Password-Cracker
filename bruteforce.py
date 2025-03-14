import zipfile
from zipfile import ZipFile


# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        print(f"[+]Password Found: {password}")
        return True
    except (RuntimeError, zipfile.BadZipfile):
        print(f"Failed attempt with password: {password}")
        return False
#     
#
zip_path = "C:\\Users\\Emma\\Documents\\Manager\\EncryptedFilePack\\enc.zip"
rock_path = "C:\\Users\\Emma\\Documents\\Manager\\EncryptedFilePack\\rockyou.txt"

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile(zip_path, 'r') as zip_file:
        with open(rock_path, 'rb') as rock_file:
            for password in rock_file:
                password = password.strip()
                if attempt_extract(zip_file, password):
                    print("[+] Extraction Successful!")
                    break
            
            # Iterate through password entries in rockyou.txt

            # Attempt to extract the zip file using each password

            # Handle correct password extract versus incorrect password attempt)

    #print("[+] Password not found in list")
if __name__ == "__main__":
    main()