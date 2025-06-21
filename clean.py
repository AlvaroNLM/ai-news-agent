import os
import shutil

# === Drop spaCy model ===
# subprocess.run(["python", "-m", "spacy", "unlink", "en_core_web_sm"])
# subprocess.run(["pip", "uninstall", "-y", "en-core-web-sm"])

# === Drop cache for HuggingFace Transformers ===
hf_cache_dir = os.path.expanduser("~/.cache/huggingface")
if os.path.exists(hf_cache_dir):
    print(f"Deleting the Transformers cache: {hf_cache_dir}")
    shutil.rmtree(hf_cache_dir)
else:
    print("There is not Transformes cache to delete.")

# === Clean .pyc and __pycache__ files ===
for root, dirs, files in os.walk("."):
    for name in files:
        if name.endswith(".pyc"):
            os.remove(os.path.join(root, name))
    for name in dirs:
        if name == "__pycache__":
            shutil.rmtree(os.path.join(root, name))

print("\n🧼 Cleaned!")