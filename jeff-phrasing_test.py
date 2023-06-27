from hypothesis import given, example, settings
from hypothesis.strategies import from_regex

import importlib
jp = importlib.import_module("jeff-phrasing")

@settings(max_examples=1000000, report_multiple_bugs=True)
@given(from_regex(jp.PARTS_MATCHER))
def test_roundtrip(outline):
    try:
        answer = jp.lookup([outline]).strip()
    except:
        pass
    else:
        assert jp.reverse_lookup(answer)
