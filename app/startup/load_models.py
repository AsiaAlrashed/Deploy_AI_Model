from sklearn.ensemble import RandomForestRegressor
import pickle


def load_traffic_model() -> RandomForestRegressor:

    file = open("./app/models/trafic_model.pkl", "rb")
    random_forest_regressor = pickle.load(file)
    file.close()

    return random_forest_regressor