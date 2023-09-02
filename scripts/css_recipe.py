import scripts.image_loader as image

class CSSRecipe:
    def __init__(self,
                 bg_image: str = ""):
        self.bg_image   = bg_image
        self.widgets    = {}

    '''
    A generic method for registering a widget to the CSSRecipe object.
    '''
    def register(self, widget_type: str, widget_id: str):
        self.widgets[widget_type]               = self.widgets[widget_type] or {}
        self.widgets[widget_type][widget_id]    = self.widgets[widget_type][widget_id] or {}

    '''
    A generic method for defining the attributes of a widget to the CSSRecipe object.
    '''
    def define_attributes(self, widget_type: str, widget_id: str, attr_dict: dict = {}):
        if (self.widgets[widget_type] is None):
            return
        if (self.widgets[widget_type][widget_id] is None):
            return
        
        widget_dict = self.widgets[widget_type][widget_id]
        for value in attr_dict.values():
            value_list                  = list(value)
            widget_dict[value_list[0]]  = value_list[1]

        del attr_dict

    
    def register_button(self, button_id: str):
        self.register("button", button_id)
        pass

    def define_button_attributes(self, button_id: str, attr_dict: dict = {}):
        self.define_attributes("button", button_id, attr_dict)

    def __str__(self):
        # Starting style
        str_builder     = ["<style>"]
        
        if (self.bg_image != ""):
            str_builder.append(
                '''
                [data-testid="stAppViewContainer"] {
                    background-image: url("data:image/png;base64,%s");
                    background-size: cover;
                }
                ''' % image.load64(self.bg_image))
        
        # Iterate through all widget types.
        for widget_type in self.widgets.values():
            # data-testid="baseButton-primary"
            pass
        
        # Ending style
        str_builder.append("</style>")
        return "\n".join(str_builder)