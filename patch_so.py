import os, struct

SO_DIR = os.environ.get("SO_DIR", "app/src/main/jniLibs/armeabi-v7a")
NEW_IP = bytes([94, 23, 168, 153])
NEW_PORT = struct.pack("<H", 2144)

OLD_IPS = [
    bytes([65, 108, 99, 34]),
    bytes([0, 0, 0, 0]),
    bytes([127, 0, 0, 1]),
]

OLD_PORTS = [
    struct.pack("<H", 2369),
    struct.pack("<H", 7777),
    struct.pack("<H", 0),
]

for filename in os.listdir(SO_DIR):
    if not filename.endswith(".so"):
        continue
    filepath = os.path.join(SO_DIR, filename)
    with open(filepath, "rb") as f:
        data = bytearray(f.read())

    patched = False
    for old_ip in OLD_IPS:
        count = data.count(old_ip)
        if count > 0:
            data = data.replace(old_ip, NEW_IP)
            patched = True
            print(f"  {filename}: IP patched ({count}x)")

    for old_port in OLD_PORTS:
        count = data.count(old_port)
        if count > 0:
            data = data.replace(old_port, NEW_PORT)
            patched = True
            print(f"  {filename}: Port patched ({count}x)")

    with open(filepath, "wb") as f:
        f.write(data)

    if not patched:
        print(f"  {filename}: Nothing to patch")
