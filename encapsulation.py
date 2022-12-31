class Anything:

  __jumlah = 0
  def __init__(self, a, b, c):
    # Public variable => bisa diakses dari luar
    self.a = a
    # Protected variable => sama dengan public variable
    self._b = b
    # Private variable => tidak bisa diakses dari luar
    self.__c = c
    
    Anything.__jumlah += 1
  
  # Hanya bisa dilakukan untuk object, bukan untuk class
  def lihat_jumlah(self):
    return self.__jumlah
    
  # Hanya bisa dilakukan untuk class, bukan untuk object
  def lihat_jumlah1():
    return Anything.__jumlah
  
  # Bisa dilakukan untuk class dan object
  @staticmethod
  def lihat_jumlah2():
    return Anything.__jumlah
  
  @classmethod
  def lihat_jumlah3(cls):
    return cls.__jumlah

  # Untuk melakukan sesuatu, buat method pass lalu jadikan property
  @property
  def nilai(self):
    pass
  
  # Properti untuk mengambil nilai seperti variabel
  @nilai.getter
  def nilai(self):
    return [self.a, self._b, self.__c]
  
  # Properti untuk mengatur nilai seperti variabel
  @nilai.setter
  def nilai(self, baru):
    list = [self.a, self._b, self.__c]
    list[0] = baru[0]
    list[1] = baru[1]
    list[1] = baru[2]
  
  # Properti untuk menghapus nilai menggunakan `del`
  @nilai.deleter
  def nilai(self):
    self.a = None
    self._b = None
    self.__c = None
