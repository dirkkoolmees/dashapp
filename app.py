{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash app running on http://127.0.0.1:8050/\n"
     ]
    }
   ],
   "source": [
    "import plotly.express as px\n",
    "from jupyter_dash import JupyterDash\n",
    "import dash_core_components as dcc\n",
    "import dash_html_components as html\n",
    "from dash.dependencies import Input, Output\n",
    "import pandas as pd\n",
    "\n",
    "external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']\n",
    "\n",
    "# Load Data\n",
    "url = 'https://raw.githubusercontent.com/dirkkoolmees/CO2_emissions_per-region/master/CO2%20Emissions%20per%20region%20-%20Sheet2.csv'\n",
    "df = pd.read_csv(url, index_col = 'Year')\n",
    "\n",
    "# Build App\n",
    "app = JupyterDash(__name__, external_stylesheets=external_stylesheets)\n",
    "server = app.server\n",
    "\n",
    "app.layout = html.Div([\n",
    "    html.H3(\"CO2 Emissions from fossil fuels and cement production\"),\n",
    "        html.Div([\n",
    "        dcc.Dropdown(\n",
    "            id='region', clearable=False,\n",
    "            value='North America', options=[\n",
    "                {'label': c, 'value': c}\n",
    "                for c in df.columns\n",
    "            ], multi = True),\n",
    "    ],style={'display': 'inline', 'width': '15%'}),\n",
    "        \n",
    "        html.Div([\n",
    "        dcc.Graph(id='graph'),\n",
    "    ],style={'display': 'inline-block', 'width': '45%'}),\n",
    "        \n",
    "        html.Div([\n",
    "        dcc.Graph(id='graph_2'),\n",
    "    ],style={'display': 'inline-block', 'width': '55%'})\n",
    "])\n",
    "# Define callback to update graph\n",
    "@app.callback(\n",
    "    [Output('graph', 'figure'),Output('graph_2', 'figure')],\n",
    "    [Input(\"region\", \"value\")]\n",
    ")\n",
    "\n",
    "def multi_output(region):\n",
    "    if region is None:\n",
    "        raise PreventUpdate\n",
    "\n",
    "    fig1 = px.line(df, x=df.index, y=region)\n",
    "    fig2 = px.area(df, x=df.index, y=region)\n",
    "    \n",
    "    fig1.update_layout(\n",
    "    yaxis_title='Thousand metric tons of C',\n",
    "    showlegend = False\n",
    "    )\n",
    "    \n",
    "    fig2.update_layout(\n",
    "    legend_title_text='Region',\n",
    "    yaxis_title='Thousand metric tons of C',\n",
    "    )\n",
    "\n",
    "    fig1.update_xaxes(showspikes=True)\n",
    "    fig1.update_yaxes(showspikes=True)\n",
    "\n",
    "    return fig1, fig2\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "# Run app\n",
    "app.run_server(debug = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
