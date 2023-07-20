def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


fixed_key = bytes.fromhex("B1EF2ACFE2BAEEFF")
final_key = bytes.fromhex("08653f75d31455c0")

print("Manager key: ",xor_data(fixed_key, final_key).hex())