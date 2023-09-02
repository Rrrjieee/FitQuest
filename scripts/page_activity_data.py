class PageActivityData:
    def __init__(self,
                 page_title: str,
                 page_icon: str = "",
                 layout: str    = "wide"):
        self.page_title     = page_title
        self.page_icon      = page_icon
        self.page_layout    = layout
