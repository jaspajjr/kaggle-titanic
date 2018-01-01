from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
import pandas as pd


def generate_surname(df):
    '''
    Gets the surname from the name column.
    '''
    df = df.copy()
    df['surname'] = df['Name'].apply(lambda x: x.split(',')[0])
    return df


def prepare_data(df):
    df = generate_surname(df)
    data = df[['Age', 'Embarked', 'Fare', 'Parch', 'PassengerId', 'Pclass',
               'Sex', 'SibSp', 'Survived', 'surname']].copy()

    data = pd.concat(
        [df, pd.get_dummies(df['Embarked']), pd.get_dummies(df['Parch']),
         pd.get_dummies(df['Pclass']), pd.get_dummies(df['Sex'])], axis=1) \
         .drop(columns=['Embarked', 'Parch', 'Sex', 'Pclass', 'Cabin', 'Name',
                        'Ticket', 'surname'], axis=1)


    # data['Sex'] = LabelEncoder().fit_transform(data['Sex'])
    # data['Age'] = np.log(data['Age'].fillna(0))
    data = data.dropna()

    return data
