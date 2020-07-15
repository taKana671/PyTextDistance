from itertools import chain
import unicodedata


class RowSizeError(Exception):
    pass


class Tabulator:

    def __init__(self, rows):
        '''rows: two-dimensional array
        '''
        self.rows = rows
        self.row_length_check()
        self.set_variables()


    def row_length_check(self):
        columns = set(len(row) for row in self.rows)
        if len(columns) > 1:
            raise RowSizeError('rows must have the same length')
   

    def set_variables(self):
        self.column_count = len(self.rows[0])
        self.row_count = len(self.rows)
        self.columns_width = self.set_columns_width()


    def width_count(self, text):
        count = 0
        for t in text:
            if unicodedata.east_asian_width(t) in 'FWA':
                count += 2
            else:
                count += 1
        return count
    
    
    def set_columns_width(self):
        return [tuple(self.width_count(str(row[i])) for row in self.rows)\
            for i in range(self.column_count)]


    def tabulate(self):
        table = []
        divider = '+'.join(['-' * (max(width) + 2) for width in self.columns_width])
        row_divider = '+' + divider + '+\n'
        table.append(row_divider)
        for i, row in enumerate(self.rows):
            table.append('|')
            for j, cell in enumerate(row):
                width = self.columns_width[j]
                max_width = max(width) 
                table.append(' {:<}{} |'.format(cell, (max_width - width[i]) * ' '))
            table.append('\n')
            table.append(row_divider)
        return ''.join(table)






        