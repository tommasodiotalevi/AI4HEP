import pandas as pd
import numpy as np
import os

def preprocess_features(muon_dataframe):
    selected_features = muon_dataframe[
      [#'Event',
    'n_Primitive',
    '1dtPrimitive.id_r',
    '2dtPrimitive.id_r',
    '3dtPrimitive.id_r',
    '4dtPrimitive.id_r',
    '1dtPrimitive.id_eta',
    '2dtPrimitive.id_eta',
    '3dtPrimitive.id_eta',
    '4dtPrimitive.id_eta',
    '1dtPrimitive.id_phi',
    '2dtPrimitive.id_phi',
    '3dtPrimitive.id_phi',
    '4dtPrimitive.id_phi',
    '1dtPrimitive.phiB',
    '2dtPrimitive.phiB',
    '3dtPrimitive.phiB',
    '4dtPrimitive.phiB',
    '1dtPrimitive.quality',
    '2dtPrimitive.quality',
    '3dtPrimitive.quality',
    '4dtPrimitive.quality',
    'delta_phi12',
    'delta_phi13',
    'delta_phi14',
    'delta_phi23',
    'delta_phi24',
    'delta_phi34'
         ]]
    processed_features = selected_features.copy()
    return processed_features.astype(np.float64)

def preprocess_targets(muon_dataframe):
    output_targets = pd.DataFrame()
    max_value = muon_dataframe["genParticle.pt"].max()
    min_value = muon_dataframe["genParticle.pt"].min()
    output_targets["genParticle.pt"] = (muon_dataframe["genParticle.pt"]-min_value)/(max_value-min_value)
    #output_targets["genParticle.pt"] = muon_dataframe["genParticle.pt"]/200.
    return output_targets.astype(np.float32)

def datasets():
    os.system("wget -q https://www.dropbox.com/s/m8ahte2xcwby8ew/bxcut_full_muon.csv")
    os.system("wget -q https://www.dropbox.com/s/9pxb63k60cz4hif/bxcut_full_test.csv")
    out_dataframe = pd.read_csv('bxcut_full_muon.csv', header=0)
    muon_dataframe_test = pd.read_csv('bxcut_full_test.csv', header=0)
    
    out_dataframe["1dtPrimitive.phiB"] = out_dataframe["1dtPrimitive.phiB"]/512.
    out_dataframe["2dtPrimitive.phiB"] = out_dataframe["2dtPrimitive.phiB"]/512.
    out_dataframe["3dtPrimitive.phiB"] = out_dataframe["3dtPrimitive.phiB"]/512.
    out_dataframe["4dtPrimitive.phiB"] = out_dataframe["4dtPrimitive.phiB"]/512.
    
    muon_dataframe_test["1dtPrimitive.phiB"] = muon_dataframe_test["1dtPrimitive.phiB"]/512.
    muon_dataframe_test["2dtPrimitive.phiB"] = muon_dataframe_test["2dtPrimitive.phiB"]/512.
    muon_dataframe_test["3dtPrimitive.phiB"] = muon_dataframe_test["3dtPrimitive.phiB"]/512.
    muon_dataframe_test["4dtPrimitive.phiB"] = muon_dataframe_test["4dtPrimitive.phiB"]/512.
    
    out_dataframe = out_dataframe[out_dataframe['genParticle.pt'] <= 200]
    muon_dataframe_test = muon_dataframe_test[muon_dataframe_test['genParticle.pt'] <= 200]
    muon_dataframe_test.to_csv("muon_test.csv")
    out_dataframe.to_csv("out_data.csv")
    return 0

def preproc(test=False):
    try:
        out_dataframe = pd.read_csv('out_data.csv')
    except FileNotFoundError:
        datasets()
        out_dataframe = pd.read_csv('out_data.csv')
    try:
        muon_dataframe_test = pd.read_csv('muon_test.csv')
    except FileNotFoundError:
        datasets()
        muon_dataframe_test = pd.read_csv('muon_test.csv')
    
    X = preprocess_features(out_dataframe)
    X_test = preprocess_features(muon_dataframe_test)
    
    Y = preprocess_targets(out_dataframe)
    Y_test = preprocess_targets(muon_dataframe_test)
    Y_test = Y_test.fillna(0)
    
    X.loc[X["1dtPrimitive.quality"] < 4, '1dtPrimitive.quality'] = 0.0
    X.loc[X["1dtPrimitive.quality"] >= 4, '1dtPrimitive.quality'] = 1.0
    X.loc[X["2dtPrimitive.quality"] < 4, '2dtPrimitive.quality'] = 0.0
    X.loc[X["2dtPrimitive.quality"] >= 4, '2dtPrimitive.quality'] = 1.0
    X.loc[X["3dtPrimitive.quality"] < 4, '3dtPrimitive.quality'] = 0.0
    X.loc[X["3dtPrimitive.quality"] >= 4, '3dtPrimitive.quality'] = 1.0
    X.loc[X["4dtPrimitive.quality"] < 4, '4dtPrimitive.quality'] = 0.0
    X.loc[X["4dtPrimitive.quality"] >= 4, '4dtPrimitive.quality'] = 1.0
    
    X_test.loc[X_test["1dtPrimitive.quality"] < 4, '1dtPrimitive.quality'] = 0.0
    X_test.loc[X_test["1dtPrimitive.quality"] >= 4, '1dtPrimitive.quality'] = 1.0
    X_test.loc[X_test["2dtPrimitive.quality"] < 4, '2dtPrimitive.quality'] = 0.0
    X_test.loc[X_test["2dtPrimitive.quality"] >= 4, '2dtPrimitive.quality'] = 1.0
    X_test.loc[X_test["3dtPrimitive.quality"] < 4, '3dtPrimitive.quality'] = 0.0
    X_test.loc[X_test["3dtPrimitive.quality"] >= 4, '3dtPrimitive.quality'] = 1.0
    X_test.loc[X_test["4dtPrimitive.quality"] < 4, '4dtPrimitive.quality'] = 0.0
    X_test.loc[X_test["4dtPrimitive.quality"] >= 4, '4dtPrimitive.quality'] = 1.0

    if test == True:
        return X_test,Y_test
    else:
        return X,Y