from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

def compare_models(models,X_train,X_test,y_train,y_test):
    results=[]; fitted={}
    for name,model in models.items():
        model.fit(X_train,y_train)
        pred=model.predict(X_test)
        results.append({
            "Model":name,
            "Accuracy":accuracy_score(y_test,pred),
            "Precision":precision_score(y_test,pred,average="weighted",zero_division=0),
            "Recall":recall_score(y_test,pred,average="weighted",zero_division=0),
            "F1 Score":f1_score(y_test,pred,average="weighted",zero_division=0)
        })
        fitted[name]=model
    return results,fitted
