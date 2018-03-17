class Table:
    def __init__(self, keys, dtypes, pkeys=None, not_null=None, indices=None):
        self.column_metadata = {key: dtype for key, dtype in zip(keys, dtypes)}
        self.columns = {key: [] for key in keys}
        self.table_max_pages = 100
        self.page_size = 4096
        self.row_size = max(self.column_metadata.values())
        self.rows_per_page = self.page_size/self.row_size
        # SQLite doesnt allow alter so there isn't any way to decrease
        # table_max_rows beneath the size of the table
        self.table_max_rows = self.rows_per_page*self.table_max_pages
        self.num_rows = 0

    def execute_insert(self, keys, values):
        for key in self.columns.keys():
            if key in keys:
                self.columns[key].append(values[keys.index(key)])
            else:
                self.columns[key].append(None)
        self.num_rows += 1

    def execute_select(self):
        'no ability to have a where clause yet or select only certain rows'
        rows = []
        rows.append(self.columns.keys())
        for i in range(len(self.num_rows)):
            row = []
            for key in self.columns.keys():
                row.append(self.columns[key][i])
            rows.append(row)
        return rows
