from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP

# Membuat key pair baru
private_key = RSA.generate(2048)

# Mengambil public key dari key pair
public_key = private_key.publickey()

# Inisialisasi objek enkripsi
cipher = PKCS1_OAEP.new(public_key)

# Teks yang akan dienkripsi
plaintext = b'Ini adalah teks yang akan dienkripsi'

# Mengenkripsi teks
ciphertext = cipher.encrypt(plaintext)
print(ciphertext)

# Inisialisasi objek dekripsi
decipher = PKCS1_OAEP.new(private_key)

# Mendekripsi teks
decrypted = decipher.decrypt(ciphertext)
print(decrypted)
