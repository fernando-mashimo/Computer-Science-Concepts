from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message('ABCDEF', 'anything but a integer')

    with pytest.raises(TypeError):
        encrypt_message(123, 6)

    # assert encrypt_message(x, y) == desired result
    assert encrypt_message('ABCD', -1) == 'DCBA'
    assert encrypt_message('ABCD', 0) == 'DCBA'
    assert encrypt_message('ABCDEF', 7) == 'FEDCBA'

    assert encrypt_message("ALGORITMO", 3) == "GLA_OMTIRO"
    assert encrypt_message('ABCDEF', 3) == 'CBA_FED'

    assert encrypt_message('ABCDEF', 4) == 'FE_DCBA'

    assert encrypt_message('', 4) == ''
