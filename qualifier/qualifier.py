from typing import Any, List, Optional


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    cntRows = len(rows)
    cntCols = len(rows[0])

    def max_width(inputs: List[List[Any]]) -> List[int]:
        width = []
        for i in range(len(inputs[0])):
            columns = []
            for j in range(len(inputs)):
                columns.append(inputs[j][i])
            width.append(max([len(str(ci)) for ci in columns]))
        return width

    def draw_body(inputs: List[List[Any]], width: List[int], centered: bool = False) -> str:
        body = ''
        for i in range(cntRows):
            for j in range(cntCols):
                cell = str(inputs[i][j])
                if centered:
                    padding = width[j] + 2 - len(cell)
                    paddingLeft = padding // 2
                    paddingRight = padding - paddingLeft
                    body += '│' + ' ' * paddingLeft + cell + ' '*paddingRight
                else:
                    body += '│ ' + cell.ljust(width[j] + 1)
            body += '│\n'
        return body.rstrip()

    def draw_head(width: List[int]) -> str:
        return '┌' + '┬'.join(['─' * (wi + 2) for wi in width]) + '┐'

    def draw_tail(width: List[int]) -> str: 
        return '└' + '┴'.join(['─' * (wi + 2) for wi in width]) + '┘'

    def draw_labels(labels: List[Any], width: List[int], centered: bool = False) -> str:
        label = ''
        for i in range(cntCols):
            cell = str(labels[i])
            if centered:
                padding = width[i] + 2 -len(cell)
                paddingLeft = padding // 2
                paddingRight = padding - paddingLeft
                label += '│' + ' ' * paddingLeft + cell + ' '*paddingRight
            else:
                label += '│ ' + cell.ljust(width[i] + 1)
        label += '│'
        separator = '├' + '┼'.join(['─' * (wi + 2) for wi in width]) + '┤'
        return label + "\n" + separator

    finaTable = ''

    if labels:
        width = max_width(rows + [labels])
        finaTable = draw_head(width) + '\n' + draw_labels(labels, width, centered) + '\n' + draw_body(rows, width, centered) + '\n' + draw_tail(width)
    else:
        width = max_width(rows)
        finaTable =  draw_head(width) + '\n' + draw_body(rows, width, centered) + '\n' + draw_tail(width)

    return finaTable
