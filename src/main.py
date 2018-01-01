import utils
import preparation
import exploration
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def main():
    df = utils.get_data()
    data = preparation.prepare_data(df)
    print data.head()

    target = data[['Survived']].copy()
    data = data.drop(columns=['Survived'], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
            data,
            target,
            test_size=0.33,
            random_state=42)
    rfc = model_fitting(X_train, y_train)

    print rfc.score(X_test, y_test)


def model_fitting(X_train, y_train):
    rfc = RandomForestClassifier()
    rfc.fit(X_train, y_train)

    return rfc

if __name__ == '__main__':
    main()
