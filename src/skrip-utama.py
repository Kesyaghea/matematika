from luas.segitiga import luas_segitiga
from luas import lingkaran, persegi
from volume.kubik import volume_kubik
import volume.bola
from volume.prisma import *

print("Luas Segitiga:", luas_segitiga(9, 6))
print("Luas Lingkaran:", lingkaran.luas_lingkaran(26))
print("Luas Persegi:", persegi.luas_persegi(28))
print("Volume Kubus:", volume_kubik(10))
print("Volume Bola:", volume.bola.volume_bola(27))
print("Volume Prisma:", volume_prisma(6, 9, 28))