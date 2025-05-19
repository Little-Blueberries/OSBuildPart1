BOOTLOADER_PATH = "build/main.bin"
IMAGE_PATH = "build/main_floopy.img"
IMAGE_SIZE = 1474560  # 1.44MB

with open(IMAGE_PATH, "wb") as img:
    img.truncate(IMAGE_SIZE)  # tạo image rỗng

with open(IMAGE_PATH, "r+b") as img:
    with open(BOOTLOADER_PATH, "rb") as boot:
        boot_sector = boot.read()
        if len(boot_sector) != 512:
            raise ValueError("Boot sector must be exactly 512 bytes!")
        img.seek(0)
        img.write(boot_sector)

print("✅ Đã tạo đĩa mềm và ghi bootloader vào sector 0.")
