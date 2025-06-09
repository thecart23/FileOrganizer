# 📁 FileOrganizer

Organizza i tuoi file in automatico come un vero pro player 🧠💻  
**FileOrganizer** è uno script Python semplice e potente che sposta i file in base alla loro estensione, rendendo la tua cartella un’oasi zen di ordine e produttività.

## 🚀 Caratteristiche

- 📂 Ordina automaticamente i file in sottocartelle per estensione
- ⚡ Veloce e semplice da usare
- 🛠️ Completamente personalizzabile
- 🧼 Mantieni pulita la tua cartella Downloads (o qualsiasi altra!)

## 🧠 Come funziona?

FileOrganizer scandaglia una directory e sposta ogni file nella relativa sottocartella, creando le cartelle se non esistono. Supporta qualsiasi tipo di estensione.

### Esempio:

Se hai questi file:

Downloads/
├── foto.png
├── documento.pdf
├── script.py

makefile
Copia
Modifica

Diventeranno:

Downloads/
├── png/
│ └── foto.png
├── pdf/
│ └── documento.pdf
├── py/
└── script.py

bash
Copia
Modifica

## 🧑‍💻 Utilizzo

1. **Clona la repo:**

```bash
git clone https://github.com/thecart23/FileOrganizer.git
cd FileOrganizer
Installa le dipendenze (se presenti):

bash
Copia
Modifica
pip install -r requirements.txt
Avvia lo script:

bash
Copia
Modifica
python file_organizer.py
Personalizza la directory da ordinare:
Modifica il valore della variabile path_to_organize nel file file_organizer.py per puntare dove ti serve.

⚙️ Personalizzazione
Vuoi che i .jpg vadano in una cartella chiamata Immagini invece di jpg?
Modifica lo script con un dizionario di mapping personalizzato. Esempio:

python
Copia
Modifica
extension_mapping = {
    'jpg': 'Immagini',
    'png': 'Immagini',
    'pdf': 'Documenti',
    'py': 'Codice'
}
🧪 To-do
 Aggiunta interfaccia grafica (GUI)

 Task scheduler integrato (es. ogni ora)

 Esclusione file temporanei/nascosti

🤝 Contribuisci
Hai idee? Bug? Apri una issue o manda una bella pull request!

🧾 Licenza
Distribuito sotto licenza MIT — libera la tua creatività ✨
Made with 💙 by thecart23
