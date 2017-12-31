from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def generate_surname(df):
    df = df.copy()
    df['surname'] = df['Name'].apply(lambda x: x.split(',')[0])
    return df

def prepare_data(df):
    df = generate_surname(df)
    data = df[['Age', 'Embarked', 'Fare', 'Parch', 'PassengerId', 'Pclass', 'Sex', 'SibSp' , 'Survived' ,'surname']].copy()


    data['Sex'] = LabelEncoder().fit_transform(data['Sex'])
    embarkation_dict = {'S': 1, 'C': 2, 'Q':3, 0: 0 }
    data['Embarked'] = data['Embarked'].fillna(0).apply(lambda x: embarkation_dict[x])
    data['Age'] = data['Age'].fillna(0)
    data['surname'] = LabelEncoder().fit_transform(data['surname'])
    data = data.dropna()

    return data