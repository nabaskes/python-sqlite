class Table:
    def __init__(self, keys, dtypes):
        self.column_metadata = {key: dtype for key, dtype in zip(keys, dtypes)}
        self.columns = {key: [] for key in keys}
