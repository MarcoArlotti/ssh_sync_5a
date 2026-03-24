import os
import re

def crea_file_md_da_txt(input_file, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)

        with open(input_file, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, start=1):
                contenuto = line.strip()

                if not contenuto:
                    continue  # salta righe vuote

                # Crea un nome file sicuro
                nome_sicuro = re.sub(r'[^a-zA-Z0-9_-]', '_', contenuto)[:50]
                nome_file = f"{nome_sicuro or f'file_{i}'}.md"

                percorso = os.path.join(output_dir, nome_file)

                with open(percorso, 'w', encoding='utf-8') as md_file:
                    md_file.write(f"# {contenuto}\n")

        print("File Markdown creati con successo!")

    except FileNotFoundError:
        print(f"Errore: il file {input_file} non esiste.")
    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    input_txt = "/home/arlo/repository/ssh_sync_5a-1/esame/sistemi/prova_pratica.txt"
    output_folder = "/home/arlo/repository/ssh_sync_5a-1/esame/sistemi"

    crea_file_md_da_txt(input_txt, output_folder)