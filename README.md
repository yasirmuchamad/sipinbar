# SIPINBAR – Sistem Informasi Peminjaman Barang Karyawan

SIPINBAR adalah aplikasi web berbasis Django untuk mencatat peminjaman dan pengembalian barang oleh karyawan. Sistem ini dilengkapi fitur validasi stok, approval oleh admin, dan pengembalian barang.

## Fitur
- Login & otorisasi user
- Daftar barang dan manajemen stok
- Pengajuan peminjaman barang (oleh user)
- Persetujuan peminjaman (oleh admin)
- Pengembalian barang (oleh admin)
- Validasi stok barang
- Daftar pinjaman per user


# Teknologi yang digunakan
- Python 3
- Django
- SQLite3
- HTML (template bawaan Django)


## Menjalankan Aplikasi (Development)
1. Clone repository ini:
   - https://github.com/yasirmuchamad/sipinbar.git
3. Install virtual environment & dependencies:
   - python -m venv venv
   - unix: source venv/bin/activate / Windows: venv\Scripts\activate
   - pip install -r requirements.txt
4. Migrasi database:
    - python manage.py makemigrations
    - python menage.py migrate
6. Jalankan server:
   - python manage.py runserver

8. Akses di browser: `http://127.0.0.1:8000/`
## Akun Login
- Admin
  - Username: admin
  - Password: admin123
- User biasa
  - Username: user
  - Password: user123

## Lisensi
Proyek ini bebas digunakan untuk keperluan belajar dan portofolio pribadi.

## Penulis
Muchamad Yasir – [GitHub](https://github.com/yasirmuchamad)

