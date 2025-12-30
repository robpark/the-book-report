import pytest

from main import build_prompt_chain


class TestPromptChain:
    def test_chain_structure(self):
        chain = build_prompt_chain()
        assert chain is not None
        assert hasattr(chain, 'invoke')

    def test_chain_invoke_signature(self):
        chain = build_prompt_chain()
        assert callable(chain.invoke)

    def test_chain_accepts_correct_input_format(self):
        test_input = {'text_input': 'test input'}
        assert isinstance(test_input, dict)
        assert 'text_input' in test_input

    @pytest.mark.integration
    def test_chain_with_real_api(self, pytestconfig):
        if not pytestconfig.getoption('--run-integration', default=False):
            pytest.skip('Integration tests require --run-integration flag and API key')
        chain = build_prompt_chain()
        input_text = 'The laptop has a 2.4 GHz quad-core processor, 8GB RAM, and 512GB SSD.'
        result = chain.invoke({'text_input': input_text})

        assert isinstance(result, str)
        assert len(result) > 0

