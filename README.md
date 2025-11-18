# GUI Comparison Report 2025

## Cara Menjalankan Demo GUI
- Pastikan Python 3.11+ sudah terpasang dan jalankan `pip install -r requirements.txt`.
- Jalankan semua contoh sekaligus dengan `run_all.bat` (Windows) atau `chmod +x run_all.sh && ./run_all.sh` (Mac/Linux).
- Atau jalankan satu per satu: `python src/01_tkinter_hello.py`, `python src/02_kivy_hello.py`, dst.

## Tips Screenshot
- Setiap window sudah berukuran ±500x300 dengan judul unik agar mudah dikenali.
- Untuk Remi, browser default akan terbuka otomatis; gunakan mode light/dark sesuai kebutuhan.
- Simpan hasil tangkapan layar di folder `screenshots/` mengikuti nama library agar rapi.

## Packaging Uji Coba
- Masuk ke folder `packaging_test/` lalu jalankan `python package_all.py`.
- Script tersebut menjalankan `pyinstaller --onefile` untuk keempat file sehingga kamu bisa memeriksa ukuran `.exe`.

## Pengisian Laporan
- Gunakan file `REPORT_TEMPLATE.docx`, ganti setiap heading dan placeholder gambar dengan isi analisis.
- Sertakan screenshot terbaik dari masing-masing GUI di bagian “Perbandingan Visual”.

