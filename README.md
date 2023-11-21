# DNS_Enumeration_Tool


This Python script performs DNS enumeration for a specified domain, retrieving various types of DNS records.

## Features

- Enumerates multiple DNS record types: A, AAAA, NS, MX, PTR, SOA.
- Handles common errors and exceptions during DNS resolution.
- Command-line usage with syntax checking.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/subdomain-enumeration.git
    cd subdomain-enumeration
    ```

2. Install dependencies:

    ```bash
    pip install dnspython
    ```

3. Run the script:

    ```bash
    python3 dns_enum.py example.com
    ```

    Replace `example.com` with the target domain.

4. The script will display information about the specified domain, including various DNS records.

## Dependencies

- [dnspython](https://www.dnspython.org/): A DNS toolkit for Python.

## Contributing

Feel free to contribute to the project by opening issues or pull requests. Your feedback and improvements are welcome!

## Credits

This project is inspired by the YouTube tutorial series [Subdomain Enumeration for Hackers](https://www.youtube.com/watch?v=SLQrbjeVrk0&list=PLa5LhaXqN29AD2HqL8Da-vORjLg5hdj_R&index=2&pp=gAQBiAQB) .


