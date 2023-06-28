from hypothesis import given, example, settings, assume
from hypothesis.strategies import from_regex

import importlib
jp = importlib.import_module("jeff-phrasing")

@settings(max_examples=10000)
# Without fullmatch here, garbage before/after the string matching the regex is added
@given(from_regex(jp.PARTS_MATCHER, fullmatch=True))
def test_roundtrip(outline):
    assume(outline)
    try:
        answer = jp.lookup([outline]).strip()
        assume(answer)
    except:
        pass
    else:
        assert jp.reverse_lookup(answer)
