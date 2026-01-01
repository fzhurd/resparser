from resparser.com.extractor.email_extractor import EmailExtractor


def test_extracts_first_email_basic():
    text = "Contact me at jane.doe@gmail.com for details."
    assert EmailExtractor().extract(text) == "jane.doe@gmail.com"


def test_returns_empty_when_no_email():
    text = "No email present here"
    assert EmailExtractor().extract(text) == ""


def test_multiple_emails_returns_first():
    text = "Primary: primary@example.com, Secondary: secondary@example.org"
    assert EmailExtractor().extract(text) == "primary@example.com"


def test_email_with_uppercase_characters():
    text = "Reach me: JOHN.DOE@EXAMPLE.COM"
    assert EmailExtractor().extract(text) == "JOHN.DOE@EXAMPLE.COM"
