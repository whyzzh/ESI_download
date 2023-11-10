import os

filePath = r'C:\Users\whyyh\Desktop\ESI_test\loop_test\test.txt'
# fileSize = os.path.getsize(filePath)
if os.path.getsize(filePath) == 0:
    os.remove(filePath)
