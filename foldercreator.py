import os

# Ana klasör adı
main_path = "/Users/erdemkismet/Desktop/Teknolojiler/Python/100days/"

# Ana klasörü oluştur
#os.makedirs(ana_klasor)

# 100 klasör oluştur
for i in range(1, 101):
    directory_name = f"day{i}"
    directory_path = os.path.join(main_path, directory_name)
    os.makedirs(directory_path)

print("Klasörler oluşturuldu.")