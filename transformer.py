import librosa
import librosa.display as display
import matplotlib.pyplot as plt
import numpy as np

#
def transformer(filepath=None, filename=None):
    
    y, sr = librosa.load(filepath + filename)
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    
    fig, ax = plt.subplots()
    img = librosa.display.specshow(
        D,
        y_axis='log',
        x_axis='time',
        ax=ax,
    )
    ax.set_title('Power spectrogram')
    fig.colorbar(img, ax=ax, format="%+2.0f dB")

    plt.savefig(filepath + filename.split('.')[0] + '.png', dpi=96)
    plt.close()

if __name__ == '__main__':
    converter(filepath='./static/uploads/', filename=None)

