from caesarcipher import CaesarCipher

# Encoding
cipher = CaesarCipher('I want to encode this string')
print(cipher.encoded)

cipher = CaesarCipher('I want to encode this string', offset=14)
print(cipher.encoded)

# Decoding
cipher = CaesarCipher('W kobh hc sbqcrs hvwg ghfwbu.', offset=14)
print(cipher.decoded)

# Cracking
cipher = CaesarCipher('O cgtz zu ktiujk znoy yzxotm.')
print(cipher.cracked)
