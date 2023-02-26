import pandas as pd
import wave

def chunk_cutter(audio_path, segments_path, output_path):
    # Read the CSV file into a DataFrame using pandas
    df = pd.read_csv(segments_path)

    # Open the audio file
    with wave.open(audio_path, 'rb') as audio_file:
        # Get the frame rate
        frame_rate = audio_file.getframerate()

        # Loop through the segments and cut the audio file into segments
        for i, row in df.iterrows():
            # Calculate the start and end frames for the current segment
            start_frame = int(row['start'] * frame_rate)
            end_frame = int(row['end'] * frame_rate)

            # Set the position in the audio file to the start frame
            audio_file.setpos(start_frame)

            # Read the data for the current segment
            segment_data = audio_file.readframes(end_frame - start_frame)

            # Do something with the segment data, such as save it to a new file with the label in the filename
            label = row['label']
            with wave.open(f'{output_path}/{i}-{label}.wav', 'wb') as segment_file:
                segment_file.setparams(audio_file.getparams())
                segment_file.writeframes(segment_data)

# def main():
#     chunk_cutter("chopsuey.wav", "segments.csv", "./")

# if(__name__ == "__main__"):
#     main()
