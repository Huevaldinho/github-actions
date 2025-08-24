from pydantic import RootModel
from typing import Dict, Any

# Using a RootModel allows us to validate a top-level dictionary as a response model.
# This is useful when the keys of the dictionary are not known in advance,
# which matches the behavior of your API.
class Data(RootModel[Dict[str, Any]]):
    pass
