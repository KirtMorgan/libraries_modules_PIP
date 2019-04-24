import os
working_dir = os.getcwd()
print(working_dir)

# Doesn't work in windows currently
# def return_user_id():
#     return (os.getuid())
# print(return_user_id())

def encode_py(file):
    return os.fsencode(file)

def decode_py(file):
    return os.fsdecode(file)

# Encoding (weak, level)
encode_name = encode_py('py_lib.py')
print(encode_name)

decode_name = decode_py(encode_name)
print(decode_name)