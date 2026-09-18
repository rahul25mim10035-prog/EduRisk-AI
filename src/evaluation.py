from sklearn.metrics import classification_report,confusion_matrix

def evaluate(model,X_test,y_test):
    pred=model.predict(X_test)
    report=classification_report(y_test,pred,output_dict=True,zero_division=0)
    matrix=confusion_matrix(y_test,pred)
    return report,matrix
