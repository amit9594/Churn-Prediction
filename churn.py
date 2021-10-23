import numpy as np
import seaborn as sns
import tensorflow as tf
import pandas as pd
def churn_prediction(Geography,Gender,age,tenure,balance,products,credit_card,active_member,estimated_salary):
    df = pd.read_csv('Churn_Modelling.csv')

    df = df.drop(['RowNumber','CustomerId','Surname'],axis=1)

    df = pd.get_dummies(df,drop_first=True)

    X = df.drop('Exited',axis=1).values
    y = df['Exited'].values

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

    from sklearn.preprocessing import StandardScaler
    Scaler = StandardScaler()
    X_train = Scaler.fit_transform(X_train)
    X_test = Scaler.transform(X_test)

    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Activation,Dropout

    model = Sequential()

    # https://stats.stackexchange.com/questions/181/how-to-choose-the-number-of-hidden-layers-and-nodes-in-a-feedforward-neural-netw


    # input layer
    model.add(Dense(11,  activation='relu'))
    # model.add(Dropout(0.2))

    # hidden layer
    model.add(Dense(6, activation='relu'))
    # model.add(Dropout(0.2))

    # output layer
    model.add(Dense(units=1,activation='sigmoid'))

    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam')

    model.fit(x=X_train, 
            y=y_train, 
            epochs=100,
            batch_size=32,
            validation_data=(X_test, y_test), 
            )
    if Gender == "Male":
        a = 1
    else:
        a = 0

    if credit_card == "Yes":
        c = 1
    else:
        c = 0
    
    if active_member == "Yes":
        b = 1
    else:
        b = 0

    if Geography == "France":
        new_data = model.predict(Scaler.transform([[1,0,0,a,age,tenure,balance,products,c,b,estimated_salary]])) > 0.5

    if Geography == "Germany":
        new_data = model.predict(Scaler.transform([[0,1,0,a,age,tenure,balance,products,c,b,estimated_salary]])) > 0.5

    if Geography == "Spain":
        new_data = model.predict(Scaler.transform([[0,0,1,a,age,tenure,balance,products,c,b,estimated_salary]])) > 0.5

    return new_data

    # if new_data == [[False]]:
    #     print('Customer will stay in bank')
    # else:
    #     print('Customer leave the bank')
    
    
    
# churn_prediction("France","Male",40,3,60000,2,"Yes","Yes",50000)
# churn_prediction(Geography,Gender,age,tenure,balance,products,credit_card,active_member,estimated_salary)