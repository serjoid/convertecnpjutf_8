import pandas as pd


def convert_csv_to_utf8(filename):
    df = pd.read_csv(filename, encoding='latin1', low_memory=False, delimiter=';', header=None)
    df.to_csv(filename, encoding='utf-8', header=None, index=False)


if __name__ == '__main__':

    filenames = [
        'F.K03200$Z.D30909.CNAECSV',
        'K3241.K03200Y0.D30909.EMPRECSV',
        'K3241.K03200Y1.D30909.EMPRECSV',
        'K3241.K03200Y2.D30909.EMPRECSV',
        'K3241.K03200Y3.D30909.EMPRECSV',
        'K3241.K03200Y4.D30909.EMPRECSV',
        'K3241.K03200Y5.D30909.EMPRECSV',
        'K3241.K03200Y6.D30909.EMPRECSV',
        'K3241.K03200Y7.D30909.EMPRECSV',
        'K3241.K03200Y8.D30909.EMPRECSV',
        'K3241.K03200Y9.D30909.EMPRECSV',
        'K3241.K03200Y0.D30909.ESTABELE',
        'K3241.K03200Y1.D30909.ESTABELE',
        'K3241.K03200Y2.D30909.ESTABELE',
        'K3241.K03200Y3.D30909.ESTABELE',
        'K3241.K03200Y4.D30909.ESTABELE',
        'K3241.K03200Y5.D30909.ESTABELE',
        'K3241.K03200Y6.D30909.ESTABELE',
        'K3241.K03200Y7.D30909.ESTABELE',
        'K3241.K03200Y8.D30909.ESTABELE',
        'K3241.K03200Y9.D30909.ESTABELE',
        'F.K03200$Z.D30909.MUNICCSV',
    ]

    for filename in filenames:
        convert_csv_to_utf8(filename)
