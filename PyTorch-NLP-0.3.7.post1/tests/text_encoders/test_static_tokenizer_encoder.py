import pickle

import pytest

from torchnlp.text_encoders import StaticTokenizerEncoder


@pytest.fixture
def input_():
    return 'This is a sentence'


@pytest.fixture
def encoder(input_):
    return StaticTokenizerEncoder([input_])


def test_static_tokenizer_encoder(encoder, input_):
    tokens = encoder.encode(input_)
    assert encoder.decode(tokens) == input_


def test_is_pickleable(encoder):
    pickle.dumps(encoder)
