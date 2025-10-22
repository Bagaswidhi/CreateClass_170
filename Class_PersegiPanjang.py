class PersegiPanjang:
    def __init__ (self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def keliling(self):
        return 2 * (self.panjang + self.lebar)
    def luas(self):
        return self.panjang * self.lebar
    def __str__(self):
        return f"Persegi Panjang dengan panjang {self.panjang} cm, dan lebar {self.lebar} cm"
    
try:
    panjang_input = int(input("Masukkan panjang (cm): "))
    lebar_input = int(input("Masukkan lebar (cm)  : "))

    pp = PersegiPanjang(panjang_input, lebar_input) # Panjang_input, lebar_input termasuk Variabel bukan parameter
    print (pp)
    print ("Keliling", pp.keliling(), "cm")
    print ("Luas", pp.luas(), "cm^2")

except ValueError:
    print("Input harus berupa angka.")   