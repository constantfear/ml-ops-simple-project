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


def get_feature_importances(n: int):
    feature_cols = [
        'сумма',
        'частота_пополнения',
        'доход',
        'сегмент_arpu',
        'частота',
        'объем_данных',
        'on_net',
        'продукт_1',
        'продукт_2',
        'зона_1',
        'зона_2',
        'секретный_скор',
        'pack_freq',
        'использование_prepared',
    ]
    model = joblib.load('models/model.pkl')
    feature_imp = {k: int(v) for k, v in zip(feature_cols,
                                             model.feature_importances_)}
    return dict(sorted(feature_imp.items(),
                       key=lambda x: x[1],
                       reverse=True)[:n])
