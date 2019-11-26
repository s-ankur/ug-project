import numpy as np
import matplotlib.pyplot as plt

def split_sequence(sequence, n_steps, n_forward=1):
    X, y = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps 
        # check if we are beyond the sequence
        if end_ix + n_forward -1 > len(sequence) - 1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix+ n_forward -1]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)

def plot_history(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()
