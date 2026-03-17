# HEIC to JPG Converter

將 HEIC 圖片轉換為 JPG 格式。

## 安裝

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
# 轉換單一檔案
python heic_to_jpg.py <file.heic>

# 轉換資料夾內所有 HEIC
python heic_to_jpg.py <folder>
```

## 轉換為 EXE

```bash
pip install pyinstaller
python -m PyInstaller --onefile heic_to_jpg.py
```

產出位置：`dist/heic_to_jpg.exe`