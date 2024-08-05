def data_recovery(data):
    # Define the headers and their corresponding file types
    headers = {
        b'\x89PNG\r\n\x1a\n': 'PNG',
        b'\xff\xd8\xff': 'JPEG',
        b'\x42\x4d': 'BMP',
        b'\x49\x49\x2a\x00': 'TIFF',
        b'\x47\x49\x46\x38': 'GIF',
        b'\x50\x4b\x03\x04': 'ZIP',
        b'\x7fELF': 'ELF',
        b'\x25\x50\x44\x46': 'PDF',
        b'\x49\x44\x33': 'MP3',
        b'\xff\xfb': 'MPEG',
        b'\x00\x00\x01\x00': 'PDDF',
        b'\x00\x01\x00\x00': 'ICO'
    }

    # List to store the detected file types
    detected_types = []

    # Iterate through the data and check for the presence of headers
    for header, file_type in headers.items():
        if header in data:
            detected_types.append(file_type)

    return detected_types


if __name__ == "__main__":
    # Example usage:
    data = b'\x89PNG\r\n\x1a\nBMII*\x00\xff\xd8\xff\xff\xd8\xff\x00\x00\x01\x00\x00'
    print(data_recovery(data))