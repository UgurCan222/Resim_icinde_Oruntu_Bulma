# PIL kütüphanesinden Image modülünü içe aktar.
from PIL import Image

# Verilen resim ve desen yolu ile deseni aramak için bir fonksiyon tanımla.
def search_pattern(image_path, pattern_path):
    # Resim ve desen yüklenir.
    img = Image.open(image_path)
    pattern = Image.open(pattern_path)

    # Desen boyutu elde edilir.
    pattern_size = pattern.size

    # Desen resmi gri tonlamalı hale getirilir.
    pattern = pattern.convert('L')

    # Desen resmi piksel verileri alınır.
    pattern_data = list(pattern.getdata())

    # Tüm eşleşmelerin koordinatlarını tutmak için bir liste oluşturulur.
    matches = []

    # Her piksel için resimde döngüye girilir.
    for y in range(img.size[1] - pattern_size[1] + 1):
        for x in range(img.size[0] - pattern_size[0] + 1):
            # Geçerli alt görüntü için piksel verileri alınır.
            sub_image = img.crop((x, y, x + pattern_size[0], y + pattern_size[1]))
            sub_data = list(sub_image.convert('L').getdata())

            # Alt görüntü ve desen için piksel verileri karşılaştırılır.
            if sub_data == pattern_data:
                # Desen bu konumda bulunmuştur.
                matches.append((x, y))

    # Tüm eşleşmeleri döndür.
    return matches

# Örnek kullanım
image_path = "c:/Users/ugurc/Desktop/image.png"
pattern_path = "c:/Users/ugurc/Desktop/oruntu.png"
result = search_pattern(image_path, pattern_path)
print(result)
