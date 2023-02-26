import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from cutHandler import chunk_cutter

def select_audio_file():
    audio_path = filedialog.askopenfilename(
        title="Selecione o arquivo de áudio",
        filetypes=(("Arquivos WAV", "*.wav"),)
    )
    audio_path_button["text"] = audio_path

def select_sections_file():
    sections_path = filedialog.askopenfilename(
        title="Selecione o arquivo CSV com as seções",
        filetypes=(("Arquivos CSV", "*.csv"),)
    )
    sections_path_button["text"] = sections_path

def select_output_directory():
    output_directory = filedialog.askdirectory(
        title="Selecione o diretório de saída"
    )
    output_directory_button["text"] = output_directory

def generate_audio_sections():
    # Obtém os caminhos dos arquivos e diretórios
    audio_path = audio_path_button["text"]
    sections_path = sections_path_button["text"]
    output_directory = output_directory_button["text"]

    if audio_path == "Selecione o arquivo de áudio" or sections_path == "Selecione o arquivo CSV com as seções" or output_directory == "Selecione o diretório de saída":
        messagebox.showerror("Erro", "Selecione todos os arquivos e diretórios necessários.")
        return

    try:
        # Gera as seções de áudio
        chunk_cutter(audio_path, sections_path, output_directory)
        messagebox.showinfo("Operação concluída", "As seções de áudio foram geradas com sucesso.")
        # Reinicializa a interface
        audio_path_button["text"] = "Selecione o arquivo de áudio"
        sections_path_button["text"] = "Selecione o arquivo CSV com as seções"
        output_directory_button["text"] = "Selecione o diretório de saída"


    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar as seções de áudio: {e}")


# Cria a janela principal
root = tk.Tk()
root.geometry("600x400") # define o tamanho da janela como 400x270 pixels
root.title("MOISES AUDIO CUTTER")
#root.configure(bg="black")

# Cria os widgets da interface
button_font = ('TkDefaultFont', 10, 'bold')


audio_path_button = tk.Button(root, text="Selecione o arquivo de áudio", command=select_audio_file, highlightthickness=0, bg="#42e0f5", relief="raised",font=button_font)
sections_path_button = tk.Button(root, text="Selecione o arquivo CSV com as seções", command=select_sections_file , highlightthickness=0, bg="#42e0f5", relief="raised",font=button_font)
output_directory_button = tk.Button(root, text="Selecione o diretório de saída", command=select_output_directory, highlightthickness=0, bg="#42e0f5", relief="raised",font=button_font)
generate_button = tk.Button(root, text="Gerar seções de áudio", command=generate_audio_sections, highlightthickness=0, bg="#00ffb3", relief="raised",font=button_font)

# Posiciona os widgets na interface
audio_path_button.pack(pady=30)
sections_path_button.pack(pady=30)
output_directory_button.pack(pady=30)
generate_button.pack(pady=30)

# Inicializa a interface
root.mainloop()