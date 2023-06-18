# 将字符串转换为字节数据
data = "0x01"
byte_data = bytes([int(data, 16)])
print(byte_data)

if __name__ == '__main__':
    pass