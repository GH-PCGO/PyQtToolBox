import binascii

import bluetooth

# 扫描所有设备
from PyQt5.QtCore import pyqtSignal
# 从common包导入hex_util
from common import hex_util
from common.hex_util import string_to_hex_string


def scan_devices():
    """
    扫描所有蓝牙设备
    :return:
    """
    print("Scanning devices...")
    device_list = []
    devices = bluetooth.discover_devices()
    for addr in devices:
        name = bluetooth.lookup_name(addr)
        # print("Found device:", name, "(", addr, ")")
        device_list.append((addr, name))
    return device_list


class BluetoothDataTransfer:
    def __init__(self, target_address, target_name, port):
        self.target_address = target_address
        self.target_name = target_name
        self.port = port
        self.socket = None

    def connect(self):
        """
        连接蓝牙设备
        :return:
        """
        try:
            self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.socket.connect((self.target_address, self.port))
            print("Connected successfully. {} ({})".format(
                self.target_name, self.target_address
            ))
        except bluetooth.BluetoothError as e:
            self.socket = None
            print("Connection failed:", str(e))

    def disconnect(self):
        """
        断开蓝牙连接
        :return:
        """
        if self.socket is not None:
            self.socket.close()
            print("Disconnected.")

    def send_data(self, data):
        """
        发送数据
        :param data:
        :return:
        """
        if self.socket is not None:
            try:
                self.socket.send(data)
                print("Data sent:", data)
            except bluetooth.BluetoothError as e:
                print("Failed to send data:", str(e))
        else:
            print("Not connected.")

    def send_hex_data(self, data):
        """
        将输入的数据转换为十六进制格式后发送到 socket
        :param data:
        """
        if self.socket is not None:
            try:
                # data = bytes([0x01])
                # self.socket.send(data)
                # 将字符串转换为字节数据
                byte_data = bytes([int(data, 16)])
                # 发送数据

                print(byte_data)
                self.socket.send(byte_data)
            except Exception as e:
                # 出现异常
                print(f"Failed to send data in HEX format: {str(e)}")
        else:
            # socket 未连接
            print("Socket is not connected.")

    def receive_data(self, buffer_size=1024):
        """
        接收数据
        :param buffer_size:
        :return:
        """
        if self.socket is not None:
            try:
                data = self.socket.recv(buffer_size)
                print("Data received:", data.decode())
                return data
            except bluetooth.BluetoothError as e:
                print("Failed to receive data:", str(e))
        else:
            print("Not connected.")

# if __name__ == '__main__':
#     print("-------------开始扫描")
#     devices = BluetoothDataTransfer.scan_devices()
#     for device in devices:
#         print(device)
#     print("-------------扫描结束")
#     bd = BluetoothDataTransfer("B7:7B:1A:07:10:0B", "PCPC", 1)  # 替换为目标设备的蓝牙地址和端口号
#     bd.connect()
#     bd.send_data("Hello, Bluetooth!")  # 发送数据
#     bd.receive_data()  # 接收数据
#     bd.disconnect()
