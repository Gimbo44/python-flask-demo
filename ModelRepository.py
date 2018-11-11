from sqlalchemy.engine import Engine

from model import Model


class ModelRepository(object):

    engine = None

    def __init__(self, engine: Engine):
        self.engine = engine

    def put(self, model: Model) -> None:
        conn = self.engine.connect()
        conn.execute(
            "INSERT INTO example(text_value, select_value) VALUES ('%s', '%s');" % (model.text_value, model.select_value)
        )
        conn.close()

    def get_model_for_id(self, model_id: int) -> Model:
        conn = self.engine.connect()
        result = conn.execute(
            "SELECT * FROM example WHERE id=%s;" % model_id
        )
        models = []
        for row in result.fetchall():
            models.append(Model(row['text_value'], row['select_value']))

        return models