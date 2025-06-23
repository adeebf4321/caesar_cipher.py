def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.

    Args:
        text (str): The input message to be processed.
        shift (int): The number of positions to shift each letter.
                     For encryption, a positive shift.
                     For decryption, a positive shift (the encryption key)
                     will automatically be converted to a negative shift
                     within the function.
        mode (str): 'encrypt' for encryption, 'decrypt' for decryption.

    Returns:
        str: The processed (encrypted or decrypted) message.
    """
    result = ""

    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift # To decrypt, we shift in the opposite direction

    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            start = ord('a') # ASCII value of 'a'
            # (ord(char) - start) gives 0 for 'a', 1 for 'b', etc.
            # Add shift, then modulo 26 to wrap around the alphabet
            # Add 'start' back to get the new ASCII value
            new_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(new_char_code)
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            start = ord('A') # ASCII value of 'A'
            new_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(new_char_code)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

def main():
    """Main function to run the Caesar Cipher program."""
    while True:
        print("\n--- Caesar Cipher Tool ---")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice in ['1', '2']:
            message = input("Enter the message: ")
            try:
                # Get shift value from user
                shift_value = int(input("Enter the shift value (an integer, e.g., 3): "))
                
                # Normalize shift to be within 0-25 for simplicity and consistency
                # A shift of 27 is the same as a shift of 1, etc.
                shift_value = shift_value % 26

                if choice == '1':
                    encrypted_message = caesar_cipher(message, shift_value, 'encrypt')
                    print(f"\nOriginal Message: {message}")
                    print(f"Shift Value: {shift_value}")
                    print(f"Encrypted Message: {encrypted_message}")
                elif choice == '2':
                    decrypted_message = caesar_cipher(message, shift_value, 'decrypt')
                    print(f"\nEncrypted Message: {message}")
                    print(f"Shift Value (used for encryption): {shift_value}")
                    print(f"Decrypted Message: {decrypted_message}")
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif choice == '3':
            print("Exiting Caesar Cipher Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

