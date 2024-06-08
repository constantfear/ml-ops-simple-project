import pandas as pd


def data_prepare(data):
    data_clean = data.copy()
    data_clean['использование_prepared'] = data['использование'].apply(
        lambda x: 1 if x == '>24LY' else 0
    )

    return data_clean


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

target_col = 'binary_target'


def import_and_prepare_data(path_to_file):

    # Get input dataframe
    print("Import data...")
    input_df = data_prepare(pd.read_csv(path_to_file))

    print("Preprocess data...")
    output_df = input_df[feature_cols]

    return output_df
