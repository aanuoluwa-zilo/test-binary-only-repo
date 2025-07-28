#!/usr/bin/env python3

# 这是一个二进制文件测试，包含Unicode字符
# This is a binary file test with Unicode characters

import struct
import random

# Generate binary data with Unicode metadata
def generate_binary_data():
    # Create binary header with Unicode info
    header = b'BINARY_TEST_测试数据'
    
    # Generate random binary data
    data = bytes([random.randint(0, 255) for _ in range(1000)])
    
    # Combine header and data
    return header + data

if __name__ == '__main__':
    binary_data = generate_binary_data()
    print(f'Generated binary data: {len(binary_data)} bytes')
    print('Binary file with Unicode metadata created!')