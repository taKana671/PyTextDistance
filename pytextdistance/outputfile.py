import csv
import os
import datetime

from xlsxwriter.workbook import Workbook


class Output:

    def __init__(self, dir, data_type):
        self.dir = os.path.abspath(dir)
        self.data_type = data_type

    def dir_check(self):
        if not os.path.isdir(self.dir):
            os.makedirs(self.dir)

    def output(self, records):
        self.dir_check()
        now = datetime.datetime.now()
        str_now = now.strftime('%Y%m%d%H%M%S')
        file_path = self.get_file(str_now)
        self.write(file_path, records)

    def write(self, *args, **kwargs):
        """Override this method in subclasses
        """
        raise NotImplementedError()

    def get_file(self, *args, **kwargs):
        """Override this method in subclasses
        """
        raise NotImplementedError()


class ExcelHandler(Output):

    def get_file(self, str_now):
        file_name = f'{self.data_type}_{str_now}.xlsx'
        return os.path.join(self.dir, file_name)

    def set_header(self, sh, keys):
        for col, key in enumerate(keys):
            sh.write_string(0, col, str(key))

    def write(self, file_path, records):
        """records: dict
        """
        keys = None
        with Workbook(file_path) as wb:
            sh = wb.add_worksheet()
            for row, record in enumerate(records, 1):
                if keys is None:
                    keys = tuple(record.keys())
                    self.set_header(sh, keys)
                for col, key in enumerate(keys):
                    sh.write(row, col, record[key])


class CsvHandler(Output):

    def get_file(self, str_now):
        file_name = f'{self.data_type}_{str_now}.csv'
        return os.path.join(self.dir, file_name)
    
    def write(self, file_path, records):
        writer = None
        with open(file_path, 'w', newline='') as f:
            for record in records:
                if writer is None:
                    writer = csv.DictWriter(f, record.keys())
                    writer.writeheader()
                writer.writerow(record)


class TextFileHandler(Output):
    
    def get_file(self, str_now):
        file_name = f'{self.data_type}_{str_now}.txt'
        return os.path.join(self.dir, file_name)

    def write(self, file_path, records):
        keys = None
        with open(file_path, 'w', encoding='utf-8') as f:
            for record in records:
                if keys is None:
                    keys = tuple(record.keys())
                    f.write(','.join(str(key) for key in keys) + '\n')
                f.write(','.join(str(record[key]) for key in keys)+ '\n')








