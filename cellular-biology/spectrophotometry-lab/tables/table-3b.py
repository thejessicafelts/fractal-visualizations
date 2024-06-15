data = {
    'Tube': ['Unknown A', 'Unknown B'],
    'Molarity': ['* 0.468', '** 0.217'],
    'Absorbance': ['0.102', '0.050'],
    'Transmittence (%)': ['79.3', '89.2']
}

df = pd.DataFrame(data)

# Display DataFrame without index using to_html
html_table = df.to_html(index=False)
display(HTML(html_table))