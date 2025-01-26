import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print("La directory non esiste.")
        return

    # Crea le cartelle per ogni tipo di file
    extensions = {
        "Immagini": [".jpg", ".jpeg", ".png", ".gif"],
        "Documenti": [".pdf", ".docx", ".txt"],
        "Audio": [".mp3", ".wav"],
        "Video": [".mp4", ".mkv"],
        "Altri": []  # File senza estensione definita
    }

    for folder in extensions.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    # Organizza i file
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            moved = False
            for folder, exts in extensions.items():
                if any(file.lower().endswith(ext) for ext in exts):
                    shutil.move(file_path, os.path.join(directory, folder, file))
                    moved = True
                    break
            if not moved:
                shutil.move(file_path, os.path.join(directory, "Altri", file))

    print("Organizzazione completata!")

# Usa la funzione
directory = input("Inserisci il percorso della directory da organizzare: ")
organize_files(directory)