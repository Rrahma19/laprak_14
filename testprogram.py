import pytest
from mainprogram import *

# ================= Penjumlahan =================
def test_penjumlahan22(): assert penjumlahan(1, 2) == 3
def test_penjumlahan23(): assert penjumlahan(-1, -2) == -3
def test_penjumlahan24(): assert penjumlahan(0, 0) == 0
def test_penjumlahan25(): assert penjumlahan(100, 200) == 300
def test_penjumlahan26(): assert penjumlahan(-10, 10) == 0
def test_penjumlahan27(): assert penjumlahan(7, -3) == 4
def test_penjumlahan28(): assert penjumlahan(-7, 3) == -4

# ================= Pengurangan =================
def test_pengurangan22(): assert pengurangan(5, 3) == 2
def test_pengurangan23(): assert pengurangan(-1, -1) == 0
def test_pengurangan24(): assert pengurangan(0, 5) == -5
def test_pengurangan25(): assert pengurangan(1000, 500) == 500
def test_pengurangan26(): assert pengurangan(3, 3) == 0
def test_pengurangan27(): assert pengurangan(-5, 5) == -10
def test_pengurangan28(): assert pengurangan(5, -5) == 10

# ================= Perkalian =================
def test_perkalian22(): assert perkalian(2, 3) == 6
def test_perkalian23(): assert perkalian(-2, 3) == -6
def test_perkalian24(): assert perkalian(0, 100) == 0
def test_perkalian25(): assert perkalian(10, -10) == -100
def test_perkalian26(): assert perkalian(-5, -5) == 25
def test_perkalian27(): assert perkalian(100, 1) == 100
def test_perkalian28(): assert perkalian(7, 0) == 0

# ================= Login =================
def test_login22(): assert login("admin", "12345") == True
def test_login23(): assert login("admin", "salah") == False
def test_login24(): assert login("user", "12345") == False
def test_login25(): assert login("", "") == False
def test_login26(): assert login("Admin", "12345") == False
def test_login27(): assert login("admin", "") == False
def test_login28(): assert login("", "12345") == False

# ================= Penambahan Tiga (pembagian) =================
def test_penambahan_tiga22(): assert penambahan_tiga(6, 2) == 3
def test_penambahan_tiga23(): assert penambahan_tiga(10, 5) == 2
def test_penambahan_tiga24(): assert penambahan_tiga(0, 1) == 0
def test_penambahan_tiga25(): assert penambahan_tiga(-10, 2) == -5
def test_penambahan_tiga26(): assert penambahan_tiga(100, 10) == 10
def test_penambahan_tiga27(): assert penambahan_tiga(-6, -2) == 3
def test_penambahan_tiga28():
    with pytest.raises(ZeroDivisionError):
        penambahan_tiga(10, 0)