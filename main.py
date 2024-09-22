import base64

while True:
    user = input("Choose option > Encode/Decode/Exit >>> ").lower()
    if user == "encode":
        user_encode = input("Write your text here >>> ")
        def encode_fun(some):
            encoded = base64.b64encode(some.encode())
            print(f"Encoded ->  {encoded}")
        encode_fun(user_encode)
    elif user == "decode":
        user_decode = input("Past cipher here >>> ")
        def decode_fun(some):
            some = some.strip("b'")
            decoded = base64.b64decode(some)
            decode_bytes = decoded.decode()
            print(decode_bytes)
        decode_fun(user_decode)
    elif user == "exit":
        print("You exit the programm")
        exit()
    else:
        print("Type error")
    