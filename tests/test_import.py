import os , sys
sys.path.append(os.getcwd())
import pytest
from typehints_checker import *

@pytest.mark.asyncio
async def test_import():
    ...