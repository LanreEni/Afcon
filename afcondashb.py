import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
from dash import dcc, html, Input, Output, callback
import numpy as np

# DATASET
data_list = [
    {'Team': 'Morocco', 'P':3, 'W':2, 'D':1, 'L':0, 'GF':6, 'GA':1, 'GD':5, 'Pts':7, 'Group':'A', 'Form':[['W','D','W']]},
    {'Team': 'Mali', 'P':3, 'W':0, 'D':3, 'L':0, 'GF':2, 'GA':2, 'GD':0, 'Pts':3, 'Group':'A', 'Form':[['D','D','D']]},
    {'Team': 'Comoros', 'P':3, 'W':0, 'D':2, 'L':1, 'GF':0, 'GA':2, 'GD':-2, 'Pts':2, 'Group':'A', 'Form':[['L','D','D']]},
    {'Team': 'Zambia', 'P':3, 'W':0, 'D':2, 'L':1, 'GF':1, 'GA':4, 'GD':-3, 'Pts':2, 'Group':'A', 'Form':[['D','D','L']]},
    {'Team': 'Egypt', 'P':3, 'W':2, 'D':1, 'L':0, 'GF':3, 'GA':1, 'GD':2, 'Pts':7, 'Group':'B', 'Form':[['W','D','W']]},
    {'Team': 'South Africa', 'P':3, 'W':2, 'D':0, 'L':1, 'GF':5, 'GA':4, 'GD':1, 'Pts':6, 'Group':'B', 'Form':[['W','L','W']]},
    {'Team': 'Angola', 'P':3, 'W':0, 'D':2, 'L':1, 'GF':2, 'GA':3, 'GD':-1, 'Pts':2, 'Group':'B', 'Form':[['D','D','L']]},
    {'Team': 'Zimbabwe', 'P':3, 'W':0, 'D':1, 'L':2, 'GF':4, 'GA':6, 'GD':-2, 'Pts':1, 'Group':'B', 'Form':[['L','D','L']]},
    {'Team': 'Nigeria', 'P':3, 'W':3, 'D':0, 'L':0, 'GF':8, 'GA':4, 'GD':4, 'Pts':9, 'Group':'C', 'Form':[['W','W','W']]},
    {'Team': 'Tunisia', 'P':3, 'W':1, 'D':1, 'L':1, 'GF':6, 'GA':5, 'GD':1, 'Pts':4, 'Group':'C', 'Form':[['W','D','L']]},
    {'Team': 'Tanzania', 'P':3, 'W':0, 'D':2, 'L':1, 'GF':3, 'GA':4, 'GD':-1, 'Pts':2, 'Group':'C', 'Form':[['D','D','L']]},
    {'Team': 'Uganda', 'P':3, 'W':0, 'D':1, 'L':2, 'GF':3, 'GA':7, 'GD':-4, 'Pts':1, 'Group':'C', 'Form':[['L','D','L']]},
    {'Team': 'Senegal', 'P':3, 'W':2, 'D':1, 'L':0, 'GF':7, 'GA':1, 'GD':6, 'Pts':7, 'Group':'D', 'Form':[['W','D','W']]},
    {'Team': 'DR Congo', 'P':3, 'W':2, 'D':1, 'L':0, 'GF':5, 'GA':1, 'GD':4, 'Pts':7, 'Group':'D', 'Form':[['W','D','W']]},
    {'Team': 'Benin', 'P':3, 'W':1, 'D':0, 'L':2, 'GF':1, 'GA':4, 'GD':-3, 'Pts':3, 'Group':'D', 'Form':[['W','L','L']]},
    {'Team': 'Botswana', 'P':3, 'W':0, 'D':0, 'L':3, 'GF':0, 'GA':7, 'GD':-7, 'Pts':0, 'Group':'D', 'Form':[['L','L','L']]},
    {'Team': 'Algeria', 'P':3, 'W':3, 'D':0, 'L':0, 'GF':7, 'GA':1, 'GD':6, 'Pts':9, 'Group':'E', 'Form':[['W','W','W']]},
    {'Team': 'Burkina Faso', 'P':3, 'W':2, 'D':0, 'L':1, 'GF':4, 'GA':2, 'GD':2, 'Pts':6, 'Group':'E', 'Form':[['W','W','L']]},
    {'Team': 'Sudan', 'P':3, 'W':1, 'D':0, 'L':2, 'GF':1, 'GA':5, 'GD':-4, 'Pts':3, 'Group':'E', 'Form':[['W','L','L']]},
    {'Team': 'Equatorial Guinea', 'P':3, 'W':0, 'D':0, 'L':3, 'GF':2, 'GA':6, 'GD':-4, 'Pts':0, 'Group':'E', 'Form':[['L','L','L']]},
    {'Team': "Côte d'Ivoire", 'P':3, 'W':2, 'D':1, 'L':0, 'GF':5, 'GA':3, 'GD':2, 'Pts':7, 'Group':'F', 'Form':[['W','D','W']]},
    {'Team': 'Cameroon', 'P':3, 'W':2, 'D':1, 'L':0, 'GF':4, 'GA':2, 'GD':2, 'Pts':7, 'Group':'F', 'Form':[['W','D','W']]},
    {'Team': 'Mozambique', 'P':3, 'W':1, 'D':0, 'L':2, 'GF':4, 'GA':5, 'GD':-1, 'Pts':3, 'Group':'F', 'Form':[['W','L','L']]},
    {'Team': 'Gabon', 'P':3, 'W':0, 'D':0, 'L':3, 'GF':4, 'GA':7, 'GD':-3, 'Pts':0, 'Group':'F', 'Form':[['L','L','L']]}
]

data = pd.DataFrame(data_list)
data["Win Rate (%)"] = (data["W"] / data["P"]) * 100

def classify_position(df):
    position_map = {}
    for group in df['Group'].unique():
        group_data = df[df['Group'] == group].sort_values('Pts', ascending=False).reset_index()
        for idx, row in group_data.iterrows():
            position_map[row['Team']] = 'Qualified' if idx <= 1 else ('Third Place' if idx == 2 else 'Eliminated')
    return df['Team'].map(position_map)

data['Status'] = classify_position(data)
qualified_teams = data[data['Status'] == 'Qualified'].sort_values('Pts', ascending=False).reset_index(drop=True)

app = dash.Dash(__name__)
app.title = "AFCON 2025 Dashboard"

colors = {
    'background': '#f5f7fa', 'card_bg': '#ffffff', 'text': '#2c3e50', 'accent': '#3498db',
    'success': '#27ae60', 'warning': '#f39c12', 'danger': '#e74c3c', 'border': '#ecf0f1',
    'secondary': '#7f8c8d'
}

card_style = {"backgroundColor": colors['card_bg'], "padding": "30px", "borderRadius": "14px", "border": f"1.5px solid {colors['border']}", "boxShadow": "0 2px 12px rgba(0, 0, 0, 0.06)", "transition": "boxShadow 0.3s ease"}
chart_style = {**card_style, "padding": "20px"}

app.layout = html.Div(
    style={"backgroundColor": colors['background'], "minHeight": "100vh", "padding": "40px 60px", "fontFamily": "'Inter', sans-serif", "color": colors['text']},
    children=[
        html.Div([html.H1("🏆 AFCON 2025 GROUP STAGE", style={"textAlign": "center", "marginBottom": "8px", "fontSize": "44px", "fontWeight": "800", "color": colors['accent'], "letterSpacing": "-0.5px"}),
                  html.P("Interactive Tournament Analytics Dashboard", style={"textAlign": "center", "color": colors['secondary'], "fontSize": "15px", "marginBottom": "50px", "letterSpacing": "0.3px"})]),
        html.Div([html.Label("Filter Groups:", style={"fontWeight": "700", "marginBottom": "16px", "display": "block", "fontSize": "15px", "color": colors['text'], "letterSpacing": "0.4px"}),
                  dcc.Checklist(id='group-filter', options=[{'label': f'  Group {g}', 'value': g} for g in ['A', 'B', 'C', 'D', 'E', 'F']], value=['A', 'B', 'C', 'D', 'E', 'F'], inline=True,
                                style={"display": "flex", "gap": "25px", "flexWrap": "wrap", "fontSize": "15px", "color": colors['text']}, inputStyle={"marginRight": "8px", "width": "18px", "height": "18px", "cursor": "pointer"})],
                 style={**card_style, "marginBottom": "40px"}),
        html.Div(id='key-stats', style={"marginBottom": "50px"}),
        html.Div(id='group-tables', style={"marginBottom": "50px"}),
        html.Div([html.Div([dcc.Graph(id='standings-chart')], style=chart_style)]),
        html.Div([html.Div([dcc.Graph(id='attack-defense-chart')], style={"flex": "1", "minWidth": "45%"}), html.Div([dcc.Graph(id='wdl-record-chart')], style={"flex": "1", "minWidth": "45%"})],
                 style={"display": "flex", "gap": "30px", "marginBottom": "40px", "flexWrap": "wrap", "justifyContent": "space-between"}),
        html.Div([html.Div([dcc.Graph(id='performance-metrics')], style=chart_style)]),
        html.Div([html.Div([dcc.Graph(id='competitiveness-chart')], style=chart_style)]),
        html.Div(id='qualified-teams-section', style={"marginTop": "40px"}),
        html.Div(id='tournament-summary', style={"marginTop": "40px"})
    ]
)

@callback(
    [Output('key-stats', 'children'), Output('group-tables', 'children'), Output('standings-chart', 'figure'),
     Output('attack-defense-chart', 'figure'), Output('wdl-record-chart', 'figure'), Output('performance-metrics', 'figure'),
     Output('competitiveness-chart', 'figure'), Output('qualified-teams-section', 'children'), Output('tournament-summary', 'children')],
    Input('group-filter', 'value')
)
def update_dashboard(selected_groups):
    filtered_data = data[data['Group'].isin(selected_groups)].copy()
    total_goals = filtered_data['GF'].sum()
    total_matches = len(filtered_data) * 3 // 2
    avg_goals = total_goals / total_matches if total_matches > 0 else 0
    highest_scorer = filtered_data.nlargest(1, 'GF').iloc[0]
    best_defense = filtered_data.nsmallest(1, 'GA').iloc[0]

    def stat_card(icon, title, value, color, value_secondary=""):
        return html.Div([html.Div(icon, style={"fontSize": "42px", "marginBottom": "14px"}), html.Div(title, style={"fontSize": "12px", "color": colors['secondary'], "marginBottom": "10px", "fontWeight": "600", "letterSpacing": "0.5px"}),
                         html.Div(value, style={"fontSize": "28px", "fontWeight": "700", "color": color, "lineHeight": "1.2"}),
                         html.Div(value_secondary, style={"fontSize": "13px", "color": color, "fontWeight": "500", "marginTop": "4px"}) if value_secondary else None],
                        style={**card_style, "textAlign": "center", "flex": "1", "transition": "transform 0.2s, boxShadow 0.2s"})

    key_stats = html.Div([html.Div([stat_card("⚽", "Total Goals", f"{total_goals}", colors['success']),
                                    stat_card("📊", "Avg Goals/Match", f"{avg_goals:.2f}", colors['accent']),
                                    stat_card("🎯", "Best Attack", f"{highest_scorer['Team']}", colors['success'], f"{highest_scorer['GF']} goals"),
                                    stat_card("🛡️", "Best Defense", f"{best_defense['Team']}", colors['accent'], f"{best_defense['GA']} conceded")],
                                  style={"display": "flex", "gap": "25px", "flexWrap": "wrap"})])

    def create_form_box(result):
        box_colors = {'W': colors['success'], 'D': colors['warning'], 'L': colors['danger']}
        return html.Span(result, style={"display": "inline-block", "width": "28px", "height": "28px", "backgroundColor": box_colors.get(result, '#64748b'), "color": "white", "textAlign": "center", "lineHeight": "28px", "borderRadius": "6px", "fontSize": "13px", "fontWeight": "700", "margin": "0 3px", "boxShadow": "0 2px 8px rgba(0, 0, 0, 0.3)"})

    group_tables = []
    for group in sorted(selected_groups):
        group_data = filtered_data[filtered_data['Group'] == group].sort_values('Pts', ascending=False).reset_index(drop=True)
        table_rows = []
        for idx, row in group_data.iterrows():
            bg_color = "rgba(39, 174, 96, 0.08)" if idx < 2 else "rgba(149, 165, 166, 0.05)"
            border_color = colors['success'] if idx < 2 else colors['border']
            gd_display = f"+{row['GD']}" if row['GD'] > 0 else str(row['GD'])
            form_list = row['Form'] if isinstance(row['Form'], list) else [row['Form']]
            form_list = [r for form in form_list for r in (form if isinstance(form, list) else [form])]
            form_boxes = [create_form_box(r) for r in form_list]
            table_rows.append(html.Tr([html.Td(f"{idx + 1}", style={"padding": "16px", "textAlign": "center", "borderBottom": f"1px solid {colors['border']}", "fontWeight": "700", "color": colors['text']}),
                                       html.Td(row['Team'], style={"padding": "16px", "textAlign": "left", "fontWeight": "700", "borderBottom": f"1px solid {colors['border']}", "fontSize": "14px", "color": colors['text']}),
                                       html.Td(row['P'], style={"padding": "16px", "textAlign": "center", "borderBottom": f"1px solid {colors['border']}", "color": colors['text']}),
                                       html.Td(row['W'], style={"padding": "16px", "textAlign": "center", "borderBottom": f"1px solid {colors['border']}", "color": colors['success'], "fontWeight": "600"}),
                                       html.Td(row['D'], style={"padding": "16px", "textAlign": "center", "borderBottom": f"1px solid {colors['border']}", "color": colors['warning'], "fontWeight": "600"}),
                                       html.Td(row['L'], style={"padding": "16px", "textAlign": "center", "borderBottom": f"1px solid {colors['border']}", "color": colors['danger'], "fontWeight": "600"}),
                                       html.Td(gd_display, style={"padding": "16px", "textAlign": "center", "color": colors['success'] if row['GD'] > 0 else colors['danger'], "fontWeight": "700", "borderBottom": f"1px solid {colors['border']}", "fontSize": "14px"}),
                                       html.Td(f"{row['GF']}:{row['GA']}", style={"padding": "16px", "textAlign": "center", "fontWeight": "700", "borderBottom": f"1px solid {colors['border']}", "color": colors['text']}),
                                       html.Td(form_boxes, style={"padding": "16px", "textAlign": "center", "borderBottom": f"1px solid {colors['border']}"}),
                                       html.Td(row['Pts'], style={"padding": "16px", "textAlign": "center", "fontWeight": "800", "fontSize": "16px", "borderBottom": f"1px solid {colors['border']}", "color": colors['accent']})],
                                      style={"backgroundColor": bg_color, "borderLeft": f"3px solid {border_color}"}))
        group_tables.append(html.Div([html.H3(f"Group {group}", style={"marginBottom": "20px", "fontSize": "22px", "fontWeight": "700", "textAlign": "center", "color": colors['accent']}),
                                      html.Table([html.Thead(html.Tr([html.Th("#", style={"padding": "16px", "textAlign": "center", "borderBottom": f"2px solid {colors['border']}", "fontWeight": "700", "fontSize": "13px", "color": colors['text']}),
                                                                       html.Th("Team", style={"padding": "16px", "textAlign": "left", "borderBottom": f"2px solid {colors['border']}", "fontWeight": "700", "fontSize": "13px", "color": colors['text']}),
                                                                       html.Th("P", style={"padding": "16px", "textAlign": "center", "borderBottom": f"2px solid {colors['border']}", "fontWeight": "700", "fontSize": "13px", "color": colors['text']}),
                                                                       html.Th("W", style={"padding": "16px", "textAlign": "center", "borderBottom": f"2px solid {colors['border']}", "fontWeight": "700", "fontSize": "13px", "color": colors['text']}),
                                                                       html.Th("D", style={"padding": "16px", "textAlign": "center", "borderBottom": f"2px solid {colors['border']}", "fontWeight": "700", "fontSize": "13px", "color": colors['text']}),
                                                                       html.Th("L", style={"padding": "16px", "textAlign": "center", "borderBottom": f"2px solid {colors['border']}", "fontWeight": "700", "fontSize": "13px", "color": colors['text']}),
                                                                       html.Th("GD", style={"padding": "16px", "textAlign": "center", "borderBottom": f"2px solid {colors['border']}", "fontWeight": "700", "fontSize": "13px", "color": colors['text']}),
                                                                       html.Th("Goals", style={"padding": "16px", "textAlign": "center", "borderBottom": f"2px solid {colors['border']}", "fontWeight": "700", "fontSize": "13px", "color": colors['text']}),
                                                                       html.Th("Form", style={"padding": "16px", "textAlign": "center", "borderBottom": f"2px solid {colors['border']}", "fontWeight": "700", "fontSize": "13px", "color": colors['text']}),
                                                                       html.Th("Pts", style={"padding": "16px", "textAlign": "center", "borderBottom": f"2px solid {colors['border']}", "fontWeight": "700", "fontSize": "13px", "color": colors['text']})])),
                                                html.Tbody(table_rows)], style={"width": "100%", "borderCollapse": "collapse", "fontSize": "13px"})],
                                     style={**card_style, "flex": "1 1 calc(33.333% - 20px)", "minWidth": "380px"}))

    group_tables_container = html.Div(group_tables, style={"display": "flex", "gap": "30px", "flexWrap": "wrap", "justifyContent": "space-between"})

    status_colors = {'Qualified': colors['success'], 'Third Place': colors['warning'], 'Eliminated': '#64748b'}
    fig_standings = go.Figure()
    for status in ['Qualified', 'Third Place', 'Eliminated']:
        status_data = filtered_data[filtered_data['Status'] == status].sort_values(['Group', 'Pts'])
        fig_standings.add_trace(go.Bar(name=status, x=status_data['Pts'], y=status_data['Team'], orientation='h', marker_color=status_colors[status], marker_line=dict(width=2, color='rgba(255,255,255,0.3)'), text=status_data['Pts'], textposition='auto', textfont=dict(size=14, color='white', family='Inter'), hovertemplate='<b>%{y}</b><br>Points: %{x}<br>Group: %{customdata}<extra></extra>', customdata=status_data['Group']))
    fig_standings.update_layout(title=dict(text="📊 Group Stage Standings", font=dict(size=24, color=colors['text'], family='Inter')), template="plotly_dark", paper_bgcolor=colors['card_bg'], plot_bgcolor=colors['card_bg'], font=dict(color=colors['text'], family='Inter', size=13), height=650, barmode='group', xaxis=dict(title="Points", title_font=dict(family='Inter', size=13), tickfont=dict(family='Inter', size=12)), yaxis=dict(title="", tickfont=dict(family='Inter', size=12)), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=13, family='Inter')), margin=dict(l=20, r=20, t=80, b=20))

    group_colors_map = {'A': '#ff3366', 'B': '#00d4ff', 'C': '#00ff88', 'D': '#ffb800', 'E': '#a855f7', 'F': '#14b8a6'}
    fig_attack_defense = go.Figure()
    for group in filtered_data['Group'].unique():
        group_data = filtered_data[filtered_data['Group'] == group]
        fig_attack_defense.add_trace(go.Scatter(x=group_data['GF'], y=group_data['GA'], mode='markers+text', name=f'Group {group}', text=group_data['Team'], textposition="top center", textfont=dict(size=11, color='white', family='Inter'), marker=dict(size=group_data['Win Rate (%)'], sizemode='diameter', sizeref=2, color=group_colors_map.get(group, colors['accent']), line=dict(width=3, color='white')), hovertemplate='<b>%{text}</b><br>Goals For: %{x}<br>Goals Against: %{y}<br>Win Rate: %{marker.size:.1f}%<extra></extra>'))
    avg_gf, avg_ga = filtered_data['GF'].mean(), filtered_data['GA'].mean()
    fig_attack_defense.add_hline(y=avg_ga, line_dash="dash", line_color=colors['warning'], line_width=2, annotation_text="Avg GA", annotation_position="right", annotation_font=dict(family='Inter', size=11))
    fig_attack_defense.add_vline(x=avg_gf, line_dash="dash", line_color=colors['success'], line_width=2, annotation_text="Avg GF", annotation_position="top", annotation_font=dict(family='Inter', size=11))
    fig_attack_defense.update_layout(title=dict(text="⚔️ Attack vs Defense Matrix", font=dict(size=22, color=colors['text'], family='Inter')), template="plotly_dark", paper_bgcolor=colors['card_bg'], plot_bgcolor=colors['card_bg'], font=dict(color=colors['text'], family='Inter', size=12), height=550, xaxis=dict(title="Goals Scored (Attack)", title_font=dict(family='Inter', size=13), tickfont=dict(family='Inter', size=12)), yaxis=dict(title="Goals Conceded (Defense)", title_font=dict(family='Inter', size=13), tickfont=dict(family='Inter', size=12)), showlegend=True, legend=dict(font=dict(size=12, family='Inter')), margin=dict(l=20, r=20, t=80, b=20))

    top_12 = filtered_data.nlargest(12, 'Pts')
    fig_wdl = go.Figure()
    fig_wdl.add_trace(go.Bar(name='Wins', x=top_12['Team'], y=top_12['W'], marker_color=colors['success'], marker_line=dict(width=2, color='rgba(255,255,255,0.3)')))
    fig_wdl.add_trace(go.Bar(name='Draws', x=top_12['Team'], y=top_12['D'], marker_color=colors['warning'], marker_line=dict(width=2, color='rgba(255,255,255,0.3)')))
    fig_wdl.add_trace(go.Bar(name='Losses', x=top_12['Team'], y=top_12['L'], marker_color=colors['danger'], marker_line=dict(width=2, color='rgba(255,255,255,0.3)')))
    fig_wdl.update_layout(title=dict(text="📈 Win-Draw-Loss Records", font=dict(size=22, color=colors['text'], family='Inter')), template="plotly_dark", paper_bgcolor=colors['card_bg'], plot_bgcolor=colors['card_bg'], font=dict(color=colors['text'], family='Inter', size=12), height=550, barmode='group', xaxis=dict(title="", tickfont=dict(family='Inter', size=11), tickangle=-45), yaxis=dict(title="Matches", title_font=dict(family='Inter', size=13), tickfont=dict(family='Inter', size=12)), legend=dict(font=dict(size=12, family='Inter')), margin=dict(l=20, r=20, t=80, b=20))

    top_8_gf = filtered_data.nlargest(8, 'GF')
    bottom_8_ga = filtered_data.nsmallest(8, 'GA')
    top_8_gd = filtered_data.nlargest(8, 'GD')
    top_8_wr = filtered_data.nlargest(8, 'Win Rate (%)')
    fig_metrics = make_subplots(rows=2, cols=2, subplot_titles=("🎯 Goals Scored", "🛡️ Best Defenses", "📊 Goal Difference", "🏆 Win Rates"), specs=[[{"type": "bar"}, {"type": "bar"}], [{"type": "bar"}, {"type": "bar"}]])
    fig_metrics.add_trace(go.Bar(x=top_8_gf['GF'], y=top_8_gf['Team'], orientation='h', marker_color=colors['success'], marker_line=dict(width=2, color='rgba(255,255,255,0.3)'), showlegend=False, text=top_8_gf['GF'], textposition='auto'), row=1, col=1)
    fig_metrics.add_trace(go.Bar(x=bottom_8_ga['GA'], y=bottom_8_ga['Team'], orientation='h', marker_color=colors['accent'], marker_line=dict(width=2, color='rgba(255,255,255,0.3)'), showlegend=False, text=bottom_8_ga['GA'], textposition='auto'), row=1, col=2)
    fig_metrics.add_trace(go.Bar(x=top_8_gd['GD'], y=top_8_gd['Team'], orientation='h', marker_color=colors['accent'], marker_line=dict(width=2, color='rgba(255,255,255,0.3)'), showlegend=False, text=top_8_gd['GD'], textposition='auto'), row=2, col=1)
    fig_metrics.add_trace(go.Bar(x=top_8_wr['Win Rate (%)'], y=top_8_wr['Team'], orientation='h', marker_color=colors['warning'], marker_line=dict(width=2, color='rgba(255,255,255,0.3)'), showlegend=False, text=[f"{x:.1f}%" for x in top_8_wr['Win Rate (%)']], textposition='auto'), row=2, col=2)
    fig_metrics.update_layout(template="plotly_dark", paper_bgcolor=colors['card_bg'], plot_bgcolor=colors['card_bg'], font=dict(color=colors['text'], family='Inter', size=12), height=750, showlegend=False, margin=dict(l=20, r=20, t=60, b=20))

    competitiveness = [np.var(filtered_data[filtered_data['Group'] == group]['Pts'].values) for group in sorted(filtered_data['Group'].unique())]
    groups_list = [f'Group {g}' for g in sorted(filtered_data['Group'].unique())]
    fig_competitiveness = go.Figure()
    fig_competitiveness.add_trace(go.Bar(x=groups_list, y=competitiveness, marker_color=[colors['accent'], colors['warning'], colors['success'], colors['danger'], colors['accent'], colors['warning']][:len(groups_list)], marker_line=dict(width=2, color='rgba(255,255,255,0.3)'), text=[f"{x:.2f}" for x in competitiveness], textposition='auto', textfont=dict(size=14, color='white', family='Inter'), hovertemplate='<b>%{x}</b><br>Competitiveness: %{y:.2f}<extra></extra>'))
    fig_competitiveness.update_layout(title=dict(text="🔥 Group Competitiveness Index", font=dict(size=24, color=colors['text'], family='Inter')), template="plotly_dark", paper_bgcolor=colors['card_bg'], plot_bgcolor=colors['card_bg'], font=dict(color=colors['text'], family='Inter', size=12), height=500, xaxis=dict(title="", tickfont=dict(family='Inter', size=11)), yaxis=dict(title="Variance (Higher = More Competitive)", title_font=dict(family='Inter', size=13), tickfont=dict(family='Inter', size=12)), margin=dict(l=20, r=20, t=80, b=20))

    qualified_filtered = qualified_teams[qualified_teams['Group'].isin(selected_groups)]
    qualified_cards = []
    for idx, (_, team) in enumerate(qualified_filtered.iterrows(), 1):
        form_list = team['Form'] if isinstance(team['Form'], list) else [team['Form']]
        form_list = [r for form in form_list for r in (form if isinstance(form, list) else [form])]
        form_boxes = [create_form_box(r) for r in form_list]
        qualified_cards.append(html.Div([html.Div(f"#{idx}", style={"fontSize": "22px", "fontWeight": "700", "color": colors['accent'], "marginBottom": "10px"}), html.Div(team['Team'], style={"fontSize": "18px", "fontWeight": "700", "marginBottom": "15px", "color": colors['text']}),
                                         html.Div([html.Div([html.Span("Group: ", style={"color": colors['secondary'], "fontSize": "13px"}), html.Span(team['Group'], style={"fontWeight": "700", "fontSize": "14px", "color": colors['accent']})], style={"marginBottom": "8px"}),
                                                   html.Div([html.Span("Points: ", style={"color": colors['secondary'], "fontSize": "13px"}), html.Span(str(team['Pts']), style={"fontWeight": "700", "fontSize": "14px", "color": colors['success']})], style={"marginBottom": "8px"}),
                                                   html.Div([html.Span("GD: ", style={"color": colors['secondary'], "fontSize": "13px"}), html.Span(f"+{team['GD']}" if team['GD'] > 0 else str(team['GD']), style={"fontWeight": "700", "fontSize": "14px", "color": colors['success'] if team['GD'] > 0 else colors['danger']})], style={"marginBottom": "8px"}),
                                                   html.Div([html.Span("Goals: ", style={"color": colors['secondary'], "fontSize": "13px"}), html.Span(f"{team['GF']}:{team['GA']}", style={"fontWeight": "700", "fontSize": "14px", "color": colors['text']})], style={"marginBottom": "12px"}),
                                                   html.Div([html.Span("Form: ", style={"color": colors['secondary'], "fontSize": "13px", "marginRight": "8px"}), html.Div(form_boxes, style={"display": "inline-block"})])])],
                                        style={**card_style, "flex": "1", "minWidth": "250px", "maxWidth": "300px"}))
    qualified_section = html.Div([html.H3("✅ QUALIFIED TEAMS (Round of 16)", style={"textAlign": "center", "marginBottom": "30px", "fontSize": "28px", "fontWeight": "700", "color": colors['text']}), html.Div(qualified_cards, style={"display": "flex", "gap": "20px", "flexWrap": "wrap", "justifyContent": "center"})], style=card_style)

    perfect_record = filtered_data[filtered_data['W'] == 3]['Team'].tolist()
    unbeaten = filtered_data[filtered_data['L'] == 0]['Team'].tolist()
    tournament_summary = html.Div([
        html.H3("📊 TOURNAMENT INSIGHTS", style={"marginBottom": "25px", "fontSize": "26px", "fontWeight": "700", "color": colors['text']}),
        html.Div([
            html.Div([html.Strong(f"🏆 Perfect Record: {', '.join(perfect_record) if perfect_record else 'None'}", style={"color": colors['accent'], "fontSize": "15px"})], style={"marginBottom": "15px"}),
            html.Div([html.Strong(f"💪 Unbeaten Teams: {', '.join(unbeaten) if unbeaten else 'None'}", style={"color": colors['accent'], "fontSize": "15px"})], style={"marginBottom": "15px"}),
            html.Div([html.Strong(f"⚽ Most Prolific: {highest_scorer['Team']} ({highest_scorer['GF']} goals)", style={"color": colors['accent'], "fontSize": "15px"})], style={"marginBottom": "15px"}),
            html.Div([html.Strong(f"🛡️ Defensive Rock: {best_defense['Team']} ({best_defense['GA']} conceded)", style={"color": colors['accent'], "fontSize": "15px"})])
        ], style={"fontSize": "14px", "lineHeight": "2"})
    ], style=card_style)

    return key_stats, group_tables_container, fig_standings, fig_attack_defense, fig_wdl, fig_metrics, fig_competitiveness, qualified_section, tournament_summary

server = app.server

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)
