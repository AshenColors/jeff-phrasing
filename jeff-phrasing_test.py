from hypothesis import given, example, settings, Verbosity
from hypothesis.strategies import from_regex

import importlib
jp = importlib.import_module("jeff-phrasing")

@settings(max_examples=1000000, verbosity=Verbosity.verbose)
# Without fullmatch here, garbage before/after the string matching the regex is added
@given(from_regex(jp.PARTS_MATCHER, fullmatch=True))
def test_roundtrip(outline):
    try:
        answer = jp.lookup([outline]).strip()
    except:
        pass
    else:
        assert jp.reverse_lookup(answer)
