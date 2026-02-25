class ReviewKomik:
    def __init__(self, judul, asal, genre, rate):
        self.judul = judul
        self.asal = asal
        self.genre = genre
        self.rate = rate

    def review_reader (self):
        print(f'Komik bergenre {self.genre} dengan judul {self.judul} yang berasal dari {self.asal} diberi rating {self.rate}')

    def ganti_rate (self, rate_baru):
        self.rate = rate_baru
        print(f'Rate terbaru dari komik {self.judul} adalah {rate_baru}')

komikSatu = ReviewKomik ('Solo Leveling', 'Korea', 'Action', '9.0')
komikDua = ReviewKomik ('Frieren Beyonds End Journey', 'Jepang', 'Fantasi', '9.35')
komikTiga = ReviewKomik ('Omniscient Reader Viewpoint', 'Korea', 'Action', '9.1')

komikSatu.ganti_rate (8.9)
komikSatu.review_reader()
komikDua.review_reader()
komikTiga.review_reader()