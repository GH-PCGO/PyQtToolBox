import binascii


def hex_string_to_bytes(hex_string: str) -> bytes:
    """
    将如下格式的字符串转成bytes字节数组
    12 F2 34 72 E2
    0x12 0xF2 0x34 0x72 0xE2
    :param hex_string: 16进制内容的字符串
    :return: 字节数组
    """
    # 去除字符串中的空格
    hex_string = hex_string.replace(" ", "")

    # 检查字符串是否包含"0x"，如果是，则去除每个字节开头的"0x"
    str_len = len(hex_string)
    if hex_string.startswith("0x"):
        # 将字符串拆分成两个字符一组的列表
        hex_list = [hex_string[i + 2:i + 4] for i in range(0, str_len, 4)]
    else:
        # 将字符串拆分成两个字符一组的列表
        hex_list = [hex_string[i:i + 2] for i in range(0, str_len, 2)]

    # 将每个十六进制字符串转换为对应的字节，并存储在字节数组中
    joined_str = "".join(hex_list)
    byte_array = bytearray.fromhex(joined_str)

    return byte_array


def bytes_to_hex_string(byte_array: bytes) -> str:
    """
    将字节数组转成16进制字符串，用空格分割。
    :param byte_array: 字节数组
    :return: 16进制字符串,以空格分割  格式如下：12 F2 34 72 E2
    """
    # 将字节数组中的每个字节转换为对应的十六进制字符串，并去除开头的"0x"
    hex_list = [hex(byte)[2:].zfill(2) for byte in byte_array]

    # 将十六进制字符串列表中的每个字符串添加空格，并连接成一个字符串
    return " ".join(hex_list).upper()


def string_to_hex_string(string: str, encoding="UTF-8") -> str:
    """
    将字符串转成16进制字符串，用空格分割。
    :param string:  字符串
    :param encoding: 字符串的转成字节数组的编码集
    :return:  16进制字符串,以空格分割, 格式如下：12 F2 34 72 E2
    """
    decode_str = binascii.hexlify(string.encode(encoding)).decode(encoding)
    # 每个两个加一个空格
    length = len(decode_str)
    decode_str_arr = [decode_str[i: i + 2] for i in range(0, length, 2)]
    return " ".join(decode_str_arr)


def hex_string_to_string(hex_string: str, encoding="UTF-8") -> str:
    """
    将16进制字符串转成字符串，如果包含0x，则自动去除0x
    :param hex_string:  16进制字符串
    :param encoding: 字符串的转成字节数组的编码集
    :return:  字符串
    """
    hex_string = hex_string.replace(" ", "")
    # 如果包含0x，则自动去除每个字节的0x
    str_len = len(hex_string)
    if hex_string.startswith("0x"):
        # 将字符串拆分成两个字符一组的列表
        hex_list = [hex_string[i + 2:i + 4] for i in range(0, str_len, 4)]
    else:
        # 将字符串拆分成两个字符一组的列表
        hex_list = [hex_string[i:i + 2] for i in range(0, str_len, 2)]
    hex_string = "".join(hex_list)

    return binascii.unhexlify(hex_string).decode(encoding)


if __name__ == '__main__':
    print("------------------------------16进制字符串=>字节数组------------------------------")
    print(hex_string_to_bytes("0x12 0xF2 0x34 0x72 0xE2"))
    print(hex_string_to_bytes("12 F2 34 72 E2"))
    print(hex_string_to_bytes("0x01"))
    print(hex_string_to_bytes("31"))

    print("------------------------------字节数组=>16进制字符串------------------------------")

    print(bytes_to_hex_string(bytes([0x12, 0xF2, 0x34, 0x72, 0xE2])))
    print(bytes_to_hex_string(b'\x12\xf24r\xe2'))
    print(bytes_to_hex_string(bytearray(b'\x12\xf24r\xe2')))

    print("-----------------------------字符串=>16进制字符串------------------------------")
    print(string_to_hex_string("abc123ABC", "gbk"))
    print("-----------------------------16进制字符串=>字符串------------------------------")
    print(hex_string_to_string("61 62 63 31 32 33 41 42 43", "gbk"))
    print(string_to_hex_string("1", "gbk"))

    message = '0x01'
    byte_message = string_to_hex_string(message).replace(' ', '')  # 将消息转换成十六进制字符串并去除空格
    byte_data = bytes.fromhex(byte_message)
    print(byte_data)

