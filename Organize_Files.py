import os
import shutil

# ================= SETTINGS =================
TARGET_DIR = r"C:\Users\James\File Organizer"  # CHANGE IF NEEDED
DRY_RUN = False # True = preview, False = move files
# ===========================================


# ---------- KEYWORD RULES (highest priority) ----------
KEYWORDS = {
    "AUTOCAD": ["autocad", "acad"],
    "INVENTOR": ["inventor", "ipt", "iam"],
    "Thunderbird": ["thunderbird"],
    "Homework": ["homework"],
    "Games": ["game", "setup", "installer"],
    "Pictures": ["img", "image", "photo", "pic", "screenshot"],
    "Videos": ["video", "recording", "movie"],
}

# ---------- EXTENSION FALLBACK RULES ----------
EXTENSIONS = {
    "AUTOCAD": [".dwg", ".dxf"],
    "INVENTOR": [".ipt", ".iam", ".idw", ".stl", ".step", ".stp"],
    "Games": [".exe", ".msi", ".iso", ".lnk"],
    "PDF": [".pdf"],
    "Pictures": [".jpg", ".jpeg", ".png", ".bmp", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
}


def get_category(filename):
    name = filename.lower()
    ext = os.path.splitext(filename)[1].lower()

    # 1️⃣ Keyword-based sorting
    for folder, words in KEYWORDS.items():
        if any(word in name for word in words):
            return folder

    # 2️⃣ Extension-based fallback
    for folder, extensions in EXTENSIONS.items():
        if ext in extensions:
            return folder

    return "Other"


def organize():
    print("=== File Organizer Started ===")

    for item in os.listdir(TARGET_DIR):
        path = os.path.join(TARGET_DIR, item)

        # Skip folders
        if not os.path.isfile(path):
            continue

        category = get_category(item)
        dest = os.path.join(TARGET_DIR, category)

        if DRY_RUN:
            print(f"[DRY RUN] {item} → {category}")
        else:
            os.makedirs(dest, exist_ok=True)
            shutil.move(path, os.path.join(dest, item))
            print(f"MOVED: {item} → {category}")

    print("=== File Organizer Finished ===")


if __name__ == "__main__":
    organize()
