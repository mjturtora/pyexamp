from .context import sample
import os

print
print '\nIn test: ', os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))

def test_examp():
    print '\nIN test_examp = ', os.path.abspath('.')
    assert len(sample.read_secrets()) == 4