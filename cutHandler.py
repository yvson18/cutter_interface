from pydub import AudioSegment
import pandas as pd
import os
import sox

def cutter_chunks(audio_path, sections_path, output_path):
    # Carrega o arquivo CSV contendo as seções
    sections = pd.read_csv(sections_path)

    # Carrega o arquivo de áudio
    #audio = AudioSegment.from_file(audio_path, format='wav')

    # Percorre as seções e cria um novo arquivo de áudio para cada seção
    i = 0
    for index, section in sections.iterrows():
        # start = section['start'] * 1000 # Converte de segundos para milissegundos
        # end = section['end'] * 1000 # Converte de segundos para milissegundos
        # label = section['label'] # Obtém o nome da seção
        # new_section = audio[start:end] # Cria uma nova seção de áudio
        
        # # Salva a nova seção em um arquivo WAV
        # file_name = f'{label}.wav'
        # file_name = os.path.join(output_path, file_name)
        # new_section.export(file_name, format='wav')
        #print(section["start"], section["end"], section["label"])
        tfm = sox.Transformer()
        tfm.trim(section["start"], section["end"])
        file_name = f"{i}-{section['label']}.wav"
        out_name = os.path.join(output_path, file_name)

        tfm.build_file(audio_path, out_name)
        i+= 1




# def main():
#     cutter_chunks("chop-suey.wav", "sections.csv", "./")

# if (__name__ == "__main__"):
#     main()
