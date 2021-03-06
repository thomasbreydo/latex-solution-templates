from solution_templates import latex_escape


def test_latex_escape():
    author = r"s\[{ \textbackslash\ ^&*~"
    assert (
        latex_escape(author)
        == r"s\textbackslash [\{\ \textbackslash textbackslash\textbackslash \ \textasciicircum \&*\textasciitilde "
    )
