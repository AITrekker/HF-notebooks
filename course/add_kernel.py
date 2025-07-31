import os
import nbformat

folder = "D:/GitHub/HF-notebooks"
kernelspec = {
    "display_name": "Python (HF-notebooks)",
    "language": "python",
    "name": "HF-notebooks"
}

for file in os.listdir(folder):
    if file.endswith(".ipynb"):
        path = os.path.join(folder, file)
        nb = nbformat.read(path, as_version=4)
        nb.metadata["kernelspec"] = kernelspec
        nbformat.write(nb, path)
        print(f"✅ Updated: {file}")
