from resparser.com.extractor.name_extractor import NameExtractor


def test_first_alpha_line_is_returned():
    text = "\n  12345 \n  --- \n   John Doe  \n Next Line"
    assert NameExtractor().extract(text) == "John Doe"


def test_trims_whitespace_from_name():
    text = "   Jane Doe   \nSomething else"
    assert NameExtractor().extract(text) == "Jane Doe"


def test_skips_blank_numeric_and_punct_only_lines():
    text = "\n\n  00000 \n *** \n Alice Wonderland"
    assert NameExtractor().extract(text) == "Alice Wonderland"


def test_empty_text_returns_empty():
    assert NameExtractor().extract("") == ""
