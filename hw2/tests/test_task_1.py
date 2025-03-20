from hw2.src.hw2.task_1 import latex_table

def full_latex_document(table_tex: str) -> str:
    return r"""\documentclass{article}
\usepackage[utf8]{inputenc}
\begin{document}
""" + table_tex + r"""
\end{document}
"""

def save_table_to_file(data, filepath):
    tex_code = latex_table(data)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(tex_code)

if __name__ == "__main__":
    sample_data = [
        ["Surname", "Name", "Age"],
        ["Ivanov", "Ivan", 22],
        ["Petrov", "Petr", 34],
        ["Fedor", "Fedorov", 29]
    ]

    tex_code = latex_table(sample_data)
    with open("../artifacts/example_table.tex", 'w', encoding='utf-8') as f:
        f.write(tex_code)

    table_tex = latex_table(sample_data)
    full_doc = full_latex_document(table_tex)
    with open("../artifacts/example_full_table.tex", 'w', encoding='utf-8') as f:
        f.write(full_doc)
