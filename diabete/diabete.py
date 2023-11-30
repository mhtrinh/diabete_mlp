
import pandas as pd
import sklearn.model_selection
import  sklearn.neural_network
import joblib

def train(csv_path,
          trained_model_path,
          test_size=0.1,
          hidden_layer=(10,10,10),
          verbose=True,
          ):
    df_org = pd.read_csv(csv_path)
    df = pd.DataFrame(columns = df_org.columns)
    target_column = df_org.columns[-1]
    predictors = list(set(list(df_org.columns))-set([target_column]))

    norm_param = df_org[predictors].max()
    df[predictors] = df_org[predictors]/norm_param
    df[target_column] = df_org[target_column]

    X = df[predictors].values
    y = df[target_column].values

    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=test_size, random_state=40)
    y_train = y_train.ravel()
    y_test = y_test.ravel()

    mlp = sklearn.neural_network.MLPClassifier(hidden_layer_sizes=hidden_layer, activation='relu', solver='adam', max_iter=500)
    mlp.fit(X_train,y_train)

    if verbose:
        from sklearn.metrics import classification_report,confusion_matrix
        predict_train = mlp.predict(X_train)
        predict_test = mlp.predict(X_test)
        print("\nTraining stats:")
        print(classification_report(y_train,predict_train))
        print("\nTest stats:")
        print(classification_report(y_test,predict_test))

    # From chatGpt:"I trained a sklearn.neural_network.MLPClassifier, How do I saved the trained model and load it and use it for inference ?"
    print(f"Saving trained model to {trained_model_path}")
    tosave = {'model': mlp,
              'norm_param': norm_param}
    joblib.dump(tosave, trained_model_path)
    return tosave


def inference(csv_input,trained_model_path):
    print(f"Loading trained model from {trained_model_path}")
    model_data = joblib.load(trained_model_path)
    model = model_data['model']
    norm_parm = model_data['norm_param']

    df = pd.read_csv(csv_input)
    x_input = df
    normed = x_input/norm_parm.values
    # print(x_input)
    # print(norm_parm.values)
    # print(normed)
    prediction = model.predict(normed.values)

    print(f"Predicted class from {csv_input}:\n{prediction}")
    return prediction






