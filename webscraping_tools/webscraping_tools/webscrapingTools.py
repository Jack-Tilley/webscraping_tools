# webscrapingTools.py
# Jack Tilley
# February 2019
# This program scrapes the inputs and outputs as a table

from bs4 import BeautifulSoup

class BaseScrape:
    def __init__(self, soupscope, table=[]):
        self.soupscope = soupscope  # takes soup argument
        self.table = table

    # cleans the data, removing spacing issues or blank lines
    def clean(self):
        for row in range(len(self.table)):
            for col in range(len(row)):
                self.table[row][col] = ' '.join(self.table[row][col].split()).replace("\n", "")
        return self.table

    # returns boolean based on whether or not the table is empty
    def table_is_empty(self):
        if self.table:
            return True
        else:
            return False


class TableScrape(BaseScrape):
    def __init__(self, soupscope, ignore_rows=[], ignore_columns=[], separated_header=True,
                 header_row_container="thead", header_row_tag="tr", table_row_container="tbody",
                 table_row_tag="tr", header_info_tag="th", table_info_tag="td", keep_all_text=False, ):
        super().__init__(soupscope)
        self.soupscope = soupscope  # takes soup argument
        self.ignore_rows = ignore_rows  # takes soup argument which will be ignored
        self.ignore_columns = ignore_columns  # takes column index arguments which will be ignored
        self.separated_header = separated_header  # True if table header and table body are separate
        self.header_row_container = header_row_container  # tag value of location where header exists in soup
        self.header_row_tag = header_row_tag  # tag value of row where header info exists
        self.table_row_container = table_row_container  # tag value of location where table exists in soup
        self.table_row_tag = table_row_tag  # tag value of where table row info exists
        self.header_info_tag = header_info_tag  # tag value of info stored inside header_row_tag
        self.table_info_tag = table_info_tag  # tag value of info stored inside table_row_tag
        self.keep_all_text = keep_all_text  # keeps first text if False, keeps all text separated by "|" if True
        self.header_data = []
        self.body_data = []
        #self.table = []

    # gets row info based on row tag
    def get_row_info(self, row, tag_to_find):
        row_list = []
        row_data = row.find_all(tag_to_find)
        for column in range(len(row_data)):
            if column not in self.ignore_columns:
                column_text_list = row_data[column].find_all(text=True)
                if self.keep_all_text:
                    column_text = "|".join(column_text_list)
                else:
                    column_text = column_text_list[0]
                row_list.append(column_text)
        return row_list

    # gets table header info
    def get_header_info(self):
        if self.separated_header:
            header_row = self.soupscope.find(self.header_row_container)
        else:
            header_row = self.soupscope.find(self.table_row_container)

        header_row = header_row.find(self.header_row_tag)
        self.header = self.get_row_info(header_row, self.header_info_tag)
        return self.header

    # gets table body info
    def get_body_info(self, rows):
        full_body_data = []
        if not self.separated_header:
            rows = rows[1:]

        for row in rows:
            if row not in self.ignore_rows:
                row_data = self.get_row_info(row, self.table_info_tag)
                self.body_data.append(row_data)
        return self.body_data

    # gets table values depending on parameters given
    def scrape(self):
        rows = self.soupscope.find(self.table_row_container).find_all(self.table_row_tag)
        full_header = self.get_header_info()
        self.table.append(full_header)
        full_body = self.get_body_info(rows)
        for info_row in full_body:
            self.table.append(info_row)
        return self.table


class ListScrape(BaseScrape):
    def __init__(self, soupscope, row_tag="li", rows_to_ignore=[], columns_to_ignore=[], keep_all=True, data_tag="div",
                 data_attr="", attr_val=""):
        super().__init__(soupscope)
        self.soupscope = soupscope  # takes soup argument
        self.row_tag = row_tag  # usually li value, list element
        self.rows_to_ignore = rows_to_ignore  # list containing indices of rows to ignore
        self.columns_to_ignore = columns_to_ignore  # list containing indices of columns to ignore
        self.keep_all = keep_all  # keeps all text if true
        self.data_tag = data_tag  # tag where data is located
        self.data_attr = data_attr  # attribute name following data_tag
        self.attr_val = attr_val  # attribute value follow data_attr

    # gets li element text
    def get_row_info(self, row):
        if not self.keep_all:
            row = row.find(self.data_tag, attrs={self.data_attr: self.attr_val})
        infolist = row.find_all(text=True)
        return [value for value in infolist if "\n" not in value or " " is not value]

    # scrapes all wanted lis
    def scrape(self):
        table = []
        rows = self.soupscope.find_all(self.row_tag)
        for row in range(len(rows)):
            if row not in self.rows_to_ignore:
                table.append(self.get_row_info(rows[row]))
        return self.table


class ContentScrape(BaseScrape):
    def __init__(self, soupscope, separate_sections=False, section_tag_value="div", section_attribute="class",
                 section_attribute_value="", item_tag_value="div", item_attribute="class", item_attribute_value="",
                 keep_image=True, keep_link=True, keep_text=True):

        super().__init__(soupscope)
        self.soupscope = soupscope  # takes soup argument
        self.separate_sections = separate_sections  # takes True if user wants sections to be separate
        self.section_tag_value = section_tag_value  # tag value of section
        self.section_attribute = section_attribute  # attribute of section
        self.section_attribute_value = section_attribute_value  # attribute value of section
        self.item_tag_value = item_tag_value  # tag value of item
        self.item_attribute = item_attribute  # item attribute
        self.item_attribute_value = item_attribute_value  # value of item attribute
        self.keep_image = keep_image  # keeps all images if true
        self.keep_link = keep_link  # keeps all links if true
        self.keep_text = keep_text  # keeps all text if true

    # gets the item from specified soup
    def get_item(self, item_soup):
        item_list = []
        if self.keep_image:
            image_list = item_soup.find_all("img")
            for image in image_list:
                item_list.append(image.get("src"))
        if self.keep_link:
            link_list = item_soup.find_all("a")  ## add initial url
            for link in link_list:
                item_list.append(link.get("href"))
        if self.keep_text:  ## working properly
            text_list = item_soup.find_all(text=True)
            for text in text_list:
                if text != "\n":
                    if "\n" in text:
                        text = text.replace("\n", "").strip()
                    item_list.append(text)
        return item_list

    # gets the section from specified soup
    def get_section(self, section_soup):  ## maybe revise
        section_list = []
        for item in section_soup:
            # print(item)
            section_list.append(self.get_item(item))
        return section_list

    # general method to scrape each item from soupscope, returning in list form
    def scrape(self):

        if self.separate_sections:  ## implement later
            pass
        #     sections = self.soupscope.find_all(self.section_tag_value,
        #                                        attrs={self.section_attribute:self.section_attribute_value})
        #     print(len(sections))
        #     for section in sections:
        #         print(type(section))
        #         content_info.append(self.get_section(section))
        else:
            items = self.soupscope.find_all(self.item_tag_value,
                                            attrs={self.item_attribute: self.item_attribute_value})
            for item in items:
                self.table.append(self.get_item(item))
        return self.table


