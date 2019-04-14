from bs4 import BeautifulSoup

class ListScrape:
    def __init__(self, soupscope, row_tag="li", rows_to_ignore=[], columns_to_ignore=[]):
        self.soupscope = soupscope  # takes soup argument
        self.row_tag = row_tag
        self.rows_to_ignore = rows_to_ignore
        self.columns_to_ignore = columns_to_ignore

    def get_row_info(self, row):
        infolist = row.find_all(text=True)
        return [value for value in infolist if "\n" not in value]


    def scrape(self):
        table = []
        rows = self.soupscope.find_all(self.row_tag)
        for row in range(len(rows)):
            if row not in self.rows_to_ignore:
                table.append(self.get_row_info(rows[row]))
        return table