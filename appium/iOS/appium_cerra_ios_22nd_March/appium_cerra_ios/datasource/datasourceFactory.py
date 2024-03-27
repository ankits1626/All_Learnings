from datasource.api import APIDatasource
from datasource.excel_data import ExcelDatasource
from datasource.json_data import JSONDatasource


class DatasourceFactory:
    @staticmethod
    def create_datasource(source_type):
        if source_type == 'api':
            return APIDatasource()
        elif source_type == 'json':
            return JSONDatasource()
        elif source_type == 'excel':
            return ExcelDatasource()
        else:
            raise ValueError(f"Invalid source type: {source_type}")
