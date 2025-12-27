from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.panel_title("Hello Shiny!"),
    ui.input_file("file",
                  "Subir fichero",
                  multiple=False,
                  button_label="fichero",
                  placeholder="No seleccion"),

    ui.input_select("seleccion",
                    "Seleciona opciones",
                    {"op1": "one piece1",
                     "op2": "one piece2",
                     "op3": "one piece3"
                    },
                     multiple=False
                    ),

    ui.input_radio_buttons("radio",
                           "Radio buttons",
                           {
                              "1" : "opcion 1",
                              "2" : "opcion 2" 
                           }),

    ui.input_slider("n", "N", 0, 100, 20),
    
)


def server(input, output, session):
    pass


app = App(app_ui, server)
