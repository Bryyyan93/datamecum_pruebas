from shiny import App, render, ui
import pandas as pd
import seaborn as sns


sns.set_theme()

# Cargas el fichero con pandas
maquina = pd.read_csv("./shiny/ejemplo3/PrediccionesMaquina.csv")

# Convertir a lista las matriculas de las maquinas
matriculas_maquinas = maquina["matricula"].unique().tolist()
# Convertir a lista las variables alarma
alarmas_maquinas = maquina.loc[:, "a1":"a203"].columns.to_list()

app_ui = ui.page_fluid(
    ui.panel_title("Ejercicio 3!"),

    ui.layout_columns(
        ui.card(
            ui.card_header("Variables"),
            ui.input_select("matricula",
                    "Matriculas de las maquinas",
                    matriculas_maquinas,
                    multiple=False),

            ui.input_select("alarma",
                    "Alarmas de las maquinas",
                    alarmas_maquinas,
                    multiple=False)
        ),

        ui.card(
            ui.card_header("Gráficos"),
            ui.h4("P_orden"),
            ui.output_plot("plot1_p_orden"),
            ui.h4("Alarma"),
            ui.output_plot("plot2_p_orden"),

        ),

        col_widths=(3, 9)
    ),

    ui.card(
        ui.card_header("Tabla"),
        ui.output_data_frame("maquina_dataframe")
    )

)

def server(input, output, session):
    @render.plot
    def plot1_p_orden():
        matri = input.matricula()
        
        sub_mach = (maquina.loc[maquina["matricula"] == matri, ["dia", "p_orden"]].sort_values("dia"))

        ax = sns.lineplot(
            data=sub_mach,
            x="dia",
            y="p_orden",
        )

    @render.plot
    def plot2_p_orden():
        matri = input.matricula()
        alarm = input.alarma()
        
        sub_mach = (maquina.loc[maquina["matricula"] == matri, ["dia", alarm]].sort_values("dia"))

        ax = sns.lineplot(
            data=sub_mach,
            x="dia",
            y=alarm,
        )
    
    @render.data_frame
    def maquina_dataframe():
        matri = input.matricula()
        filtro = maquina.loc[maquina["matricula"] == matri]
        return render.DataGrid(filtro.loc[:,"a1":"a203"])


app = App(app_ui, server)
