# PyCypher - SAY-Format Encryption

PyCypher is a Python-based tool developed by Sayantan Patra for encrypting text messages securely using the SAY-Format Encryption algorithm. With PyCypher, you can ensure the confidentiality and integrity of your sensitive information by transforming it into an unreadable format using a unique encryption key.

## Features

- **SAY-Format Encryption**: Encrypt your messages using the SAY-Format Encryption algorithm, ensuring that only authorized users with the decryption key can access the original text.
- **Token Generation**: PyCypher generates a unique token for each encryption, which serves as a reference for decryption.
- **Database Integration**: Utilizes MySQL database for storing encryption keys securely.
- **User-friendly Interface**: Terminal-based interface for easy interaction and seamless user experience.

## Getting Started

To use PyCypher for SAY-Format Encryption, follow these simple steps:
## Getting Started

To use PyCypher for SAY-Format Encryption, follow these simple steps:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/sayantancodex/PyCypher.git
  
2. Install the required dependencies by running:

   ```bash
   pip install -r requirements.txt
3. Configure the MySQL database by updating the `dbconfig.ini` file with your database credentials.
4. Run the `main.py` file to start PyCypher.
    ```bash
     python3 main.py
5. Choose the encryption option and enter your message to be encrypted.
6. PyCypher will generate a unique token and encrypt the message using the SAY-Format Encryption algorithm.
7. Copy and save the token for decryption later.

## Usage

### Encryption

1. Select the encryption option from the menu.
2. Enter your message to be encrypted.
3. PyCypher will generate a unique token and encrypt the message using the SAY-Format Encryption algorithm.
4. Copy and save the token for decryption later.

### Decryption

1. Select the decryption option from the menu.
2. Enter the decryption token received during encryption.
3. PyCypher will retrieve the corresponding key from the database and decrypt the message.
4. Enjoy the decrypted message!

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.

## Contact

For any queries or support, you can reach out to Sayantan Patra at [sayantanpatra68@gmail.com](mailto:sayantanpatra68@gmail.com).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
