import pandas as pd
import joblib


# Make prediction
def make_pred(dt, path_to_file):

    print('Importing pretrained model...')

    model = joblib.load('models/model.pkl')

    # Define optimal threshold
    model_th = 0.32323232323232326

    # Make submission dataframe
    submission = pd.DataFrame({
        'client_id':  pd.read_csv(path_to_file)['client_id'],
        'preds': (model.predict_proba(dt)[:, 1] > model_th) * 1
    })

    print('Prediction complete!')

    # Return proba for positive class
    return submission
