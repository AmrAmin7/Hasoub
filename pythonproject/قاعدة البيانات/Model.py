class Model:

    db = None
    connection = None

    def __init__(self):
        self._create_table()
        self._saved =False

    @classmethod
    def _get_table_name(cls):
        return cls.__name__.lower()

    @classmethod
    def get_columns(cls):
        columns ={}
        for key ,value in cls.__dict__.items():
            if str(key).startswith('_'):
                continue
            columns[str(key)] = str(value)
        return columns
    #هتمر الحلقة على كل ما يعرفه القاموس dict ويمرره فى columns ويثتثنى منه كل ما يبدأ _
    # وهذا يعنى ان اعمدة الجدول ستمثل بخصائص عامة و باقى الجدول هتكون private

    def _create_table(self):
       columns = ', '.join(' '.join((key, value)) for (key, value) in self.get_columns().items())
       sql = f'CREATE TABLE IF NOT EXISTS {self._get_table_name()} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns})'
       cursor = self.connection.cursor()
       result = cursor.execute(sql)
       return result


