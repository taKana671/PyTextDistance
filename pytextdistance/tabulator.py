from itertools import chain

class Tabulator:

    def __init__(self, items, rows=2):
        self.rows = rows
        self.columns = len(items)
        self.items = tuple(item for item in chain(items.keys(), items.values()))


    def tabulate(self):
        table = []
        row = column = column_width = 0
        for item in self.items:
            column_width = max(column_width, len(str(item)))
        divider = ('-' * (column_width + 2)) + '+'
        row_divider = '+' + (divider * self.columns) + '\n'
        table.append(row_divider)
        for item in self.items:
            if column == 0:
                table.append('|')
            table.append(' {:<{}} |'.format(item, column_width))
            column += 1
            if column == self.columns:
                table.append('\n')
                row += 1
                if row < self.rows:
                    table.append(row_divider)
            column %= self.columns
        table.append(row_divider)
        return ''.join(table)



        