data = {
    'Tube': ['1', '2', '3', '4', '5', '6'],
    'Molarity': [1.00, 0.50, 0.25, 0.125, 0.0125, 0.00125],
    'Absorbance': [0.218, 0.095, 0.061, 0.026, 0.020, 0.001],
    'Transmittence (%)': [60.5, 80.4, 86.9, 94.2, 99.4, 99.8]
}

df = pd.DataFrame(data)

# Display DataFrame without index using to_html
html_table = df.to_html(index=False)
display(HTML(html_table))