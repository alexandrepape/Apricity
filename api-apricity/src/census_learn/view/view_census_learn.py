from flask_restful import Resource, abort
from src.configuration.session import session
from src.census_learn.model.model_census_lean import Census_learn_sql
from collections import defaultdict

class Census(Resource):
    def get(self, col_name):
        try:
            value = session.query(Census_learn_sql.__table__.c[col_name], Census_learn_sql.age).filter(
                Census_learn_sql.education is not None).filter(Census_learn_sql.age is not None).all()
        except :
            abort(404, message='Données non existante')

        d = defaultdict(list)

        # regroupent les données en dictionnaire
        for x, y in value:
            d[x].append(y)


        # supprime toutes les données None
        t = {k: v for k, v in d.items() if v is not None and k is not None}

        # compte la moyenne des ages dans le dictionnaire
        avgDict = {}
        for k, v in t.items():
            avgDict[k] = round((sum(v) / float(len(v))), 2)

        # liste les donnée et compte les valeurs distinct
        data_v = [item[0] for item in value if item[0] is not None]
        result_value_distinct = [[x, data_v.count(x)] for x in set(data_v)]

        # créer un dictionnaire pour la vue qui regroupe tout
        count = 0
        i = 1
        dict_f = {}
        for key, val in avgDict.items():
            for x in result_value_distinct:
                if x[0] == key:
                    count = x[1]
            dict_f[i] = {
                            "value": key,
                            "avg_age": val,
                            "count": count
                           }
            i += 1
        return dict_f
