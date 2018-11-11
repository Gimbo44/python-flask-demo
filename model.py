class Model(object):

    text_value = ''
    select_value = ''

    def __init__(self, text_value: str, select_value: str) -> None:
        self.text_value = text_value
        self.select_value = select_value
