# Program: Siklus Kerja CPU (Fetch - Decode - Execute - Store)
# Dibuat oleh Nursania D Koda

import time

def fetch():
    print("1️⃣ FETCH: Mengambil instruksi dari memori...")
    time.sleep(1)
    instruction = "ADD A, B"
    print(f"Instruksi diambil: {instruction}")
    return instruction

def decode(instruction):
    print("\n2️⃣ DECODE: Menerjemahkan instruksi...")
    time.sleep(1)
    operation, operands = instruction.split()[0], instruction.split()[1]
    print(f"Operasi: {operation}, Operan: {operands}")
    return operation, operands

def execute(operation, operands):
    print("\n3️⃣ EXECUTE: Menjalankan instruksi...")
    time.sleep(1)
    if operation == "ADD":
        print(f"Menambahkan nilai pada {operands}")
    else:
        print("Operasi tidak dikenal.")
    result = "Hasil disimpan di register A"
    return result

def store(result):
    print("\n4️⃣ STORE: Menyimpan hasil ke memori...")
    time.sleep(1)
    print(result)

def main():
    print("=== SIMULASI SIKLUS KERJA CPU ===\n")
    instruksi = fetch()
    operasi, operan = decode(instruksi)
    hasil = execute(operasi, operan)
    store(hasil)
    print("\n=== Program Selesai ===")
    print("💻 Dibuat oleh Nursania D Koda 💻")

if __name__ == "__main__":
    main()
