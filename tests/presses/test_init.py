from pytest import raises

from edition.exceptions import NoPressError
from edition.presses import make


def test_make__unregistered_key() -> None:
    with raises(NoPressError) as ex:
        make(key="foo", markdown_content="")
    assert str(ex.value) == 'No press for "foo"'
