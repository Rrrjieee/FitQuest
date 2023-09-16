from flask import Flask, Response, render_template_string, url_for
from scripts.exercise import BaseExercise

def user_custom_routine(app: Flask, exer_list: list):
    count_cfg   = {
        'left'  : 3.4,
        'top'   : 3.4,
        'col'   : 4,
    }
    with app.app_context():
        css = render_template_string(
            open("static/css/user_custom_routine_base.css").read()
        )

        has_top_field   = False
        top_margin      = 0
        for index in range(1,5):
            # Generate CSS for each button dynamically
            css += f"""
            .field_space#exercise .option#btn-{index} {{
            """
            top_margin      = ((index - 1) // 2)
            has_top_field   = (top_margin > 0)
            top_margin     *= 9
            if (has_top_field):
                css        += f"""
                top: """ + str(top_margin) + "vw;" + f"""
                """
            
            if (index % 2 == 0):
                css += f"""
                left: 9vw;
                """
            
            img_link    = url_for("static", filename=exer_list[index-2].img_path)
            css += f"""
                background-image: url("{img_link}");
                background-size: 100% 100%;
            }}
            """

        
        for index in range(1,13):
            # Generate CSS for each button dynamically
            css += f"""
            .field_space#count .option#btn-{index} {{
            """
            top_margin      = ((index - 1) // count_cfg["col"])
            has_top_field   = (top_margin > 0)
            top_margin     *= count_cfg["top"]
            if (has_top_field):
                css        += f"""
                top: {top_margin}vw;
                """
            
            pos         = (index % count_cfg["col"]) - 1
            if (pos < 0):
                pos    += count_cfg["col"]

            pos        *= count_cfg["left"]
            css        += f"""
            left: {pos}vw;
            """
            
            css += f"""
            }}
            """

        # Return the generated CSS as a response with the appropriate content type
        return Response(css, content_type='text/css')