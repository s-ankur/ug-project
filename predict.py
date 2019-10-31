import numpy as np

from dataset import suny_international
from animate import plot_daily

from keras.models import load_model


if __name__ == "__main__":

    df=suny_international.load_data()

    X=np.array(df.index.minute+df.index.hour*60).reshape(-1,1)
    y=np.array(df['GHI'])
    model = load_model('models/simple_dnn_daily.h5')
    y_pred = model.predict(X)
    plot_daily(y ,y_pred.ravel(),save='media/simple_dnn_daily.mp4', index=df.index)
    
    X=np.array([df.index.minute+df.index.hour*60,df.index.month]).T
    y=np.array(df['GHI'])
    model = load_model('models/simple_dnn_monthly.h5')
    y_pred = model.predict(X)
    plot_daily(y ,y_pred.ravel(),save='media/simple_dnn_monthly.mp4', index=df.index)

    X=np.array([df.index.minute+df.index.hour*60, df.index.month,
            *(df[factor] for factor in suny_international.atmospheric_factors)]).T
    y=np.array(df['GHI'])
    model = load_model('models/simple_dnn_atmospheric.h5')
    y_pred = model.predict(X)
    plot_daily(y ,y_pred.ravel(),save='media/simple_dnn_atmoshperic.mp4', index=df.index)
