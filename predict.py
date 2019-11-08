import numpy as np
import warnings
import tensorflow as tf

from dataset import suny_international
from animate import plot_daily
from utility import split_sequence
from keras.models import load_model

warnings.filterwarnings("ignore")
tf.get_logger().setLevel('ERROR')


if __name__ == "__main__":

    df=suny_international.load_data()
    plot_daily(df['GHI'],save='media/GHI.mp4', index=df.index)
    df_train,df_test = suny_international.train_test_split(df)
    
    X=np.array(df_test.index.minute+df_test.index.hour*60).reshape(-1,1)
    y=np.array(df_test['GHI'])
    model = load_model('models/simple_dnn_daily.h5')
    y_pred = model.predict(X)
    plot_daily(y ,y_pred.ravel(),save='media/simple_dnn_daily.mp4', index=df_test.index)

    X=np.array([df_test.index.minute+df_test.index.hour*60,df_test.index.month]).T
    y=np.array(df_test['GHI'])
    model = load_model('models/simple_dnn_monthly.h5')
    y_pred = model.predict(X)
    plot_daily(y ,y_pred.ravel(),save='media/simple_dnn_monthly.mp4', index=df_test.index)

    X=np.array([df_test.index.minute+df_test.index.hour*60, df_test.index.month,
            *(df_test[factor] for factor in suny_international.atmospheric_factors)]).T
    y=np.array(df_test['GHI'])
    model = load_model('models/simple_dnn_atmospheric.h5')
    y_pred = model.predict(X)
    plot_daily(y[] ,y_pred.ravel(),save='media/simple_dnn_atmoshperic.mp4', index=df_test.index)

    n_features = 1
    n_steps = 20 
    X, y = split_sequence(df_test['GHI'], n_steps)
    X = X.reshape((X.shape[0], X.shape[1], n_features))
    model = load_model('models/simple_rnn.h5')
    y_pred = model.predict(X)
    plot_daily(y ,y_pred.ravel(),save='media/simple_rnn.mp4', index=df_test.index[n_steps:])
