from bs4 import BeautifulSoup

class ContentScrape:
    def __init__(self, soupscope, separate_sections=False, section_tag_value="div", section_attribute="class",
                 section_attribute_value="",item_tag_value="div", item_attribute="class", item_attribute_value="",
                 keep_image=True, keep_link=True, keep_text=True):

        self.soupscope = soupscope  # takes soup argument
        self.separate_sections = separate_sections # takes True if user wants sections to be separate
        self.section_tag_value = section_tag_value # tag value of section
        self.section_attribute = section_attribute # attribute of section
        self.section_attribute_value = section_attribute_value # attribute value of section
        self.item_tag_value = item_tag_value # tag value of item
        self.item_attribute = item_attribute # item attribute
        self.item_attribute_value = item_attribute_value # value of item attribute
        self.keep_image = keep_image # keeps all images if true
        self.keep_link = keep_link # keeps all links if true
        self.keep_text = keep_text # keeps all text if true

    # gets the item from specified soup
    def get_item(self, item_soup):
        item_list = []
        if self.keep_image:
            image_list = item_soup.find_all("img")
            for image in image_list:
                item_list.append(image.get("src"))
        if self.keep_link:
            link_list = item_soup.find_all("a") ## add initial url
            for link in link_list:
                item_list.append(link.get("href"))
        if self.keep_text: ## working properly
            text_list = item_soup.find_all(text=True)
            for text in text_list:
                if text != "\n":
                    if "\n" in text:
                        text = text.replace("\n","").strip()
                    item_list.append(text)
        return item_list

    # gets the section from specified soup
    def get_section(self, section_soup): ## maybe revise
        section_list = []
        for item in section_soup:
            # print(item)
            section_list.append(self.get_item(item))
        return section_list

    # general method to scrape each item from soupscope, returning in list form
    def scrape(self):
        content_info = []
        if self.separate_sections: ## implement later
            pass
        #     sections = self.soupscope.find_all(self.section_tag_value,
        #                                        attrs={self.section_attribute:self.section_attribute_value})
        #     print(len(sections))
        #     for section in sections:
        #         print(type(section))
        #         content_info.append(self.get_section(section))
        else:
            items = self.soupscope.find_all(self.item_tag_value,
                                            attrs={self.item_attribute:self.item_attribute_value})
            for item in items:
                content_info.append(self.get_item(item))
        return content_info
