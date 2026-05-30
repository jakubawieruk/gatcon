import pytest

from gatcon import isIdValid, validServer


@pytest.mark.parametrize(
    "board_id, expected",
    [
        ("123456", True),
        ("12345", False),
        ("1234567", False),
        ("", False),
    ],
)
def test_is_id_valid_checks_length(board_id, expected):
    assert isIdValid(board_id) is expected


def test_valid_server_accepts_any_value():
    # validServer is currently a stub that accepts everything; this documents
    # the present behaviour so a future tightening is a deliberate change.
    assert validServer("lns.example.com") is True
