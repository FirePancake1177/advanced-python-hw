from hw2 import task_1, task_2

sample_data = [
    ["Surname", "Name", "Age"],
    ["Ivanov", "Ivan", 22],
    ["Petrov", "Petr", 34],
    ["Fedor", "Fedorov", 29]
]

table_tex = task_1.latex_table(sample_data)
figure_tex = task_2.latex_figure("pic.png", caption="Pic example", label="fig:example")

full_tex = f"""\\documentclass{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage{{graphicx}}

\\begin{{document}}

{table_tex}

\\bigskip

{figure_tex}

\\end{{document}}
"""

with open("example_full.tex", 'w', encoding='utf-8') as f:
    f.write(full_tex)