import time

data = [500]

print("=== UJI RESOURCE LIMIT DOCKER ===")

try:
    i = 0
    while True:
        i += 1

        # Bebani CPU
        x = i * i * i

        # Alokasi memori bertahap (1 MB)
        data.append("X" * 1024 * 1024)

        print(f"Iterasi: {i} | Memori terpakai: {len(data)} MB")
        time.sleep(0.1)

except MemoryError:
    print("ERROR: Memori tidak mencukupi!")

except Exception as e:
    print("Program dihentikan:", e)