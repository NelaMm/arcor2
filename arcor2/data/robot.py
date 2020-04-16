from dataclasses import dataclass, field

from dataclasses_jsonschema import JsonSchemaMixin


@dataclass
class RobotFeatures(JsonSchemaMixin):

    focus: bool = False


@dataclass
class RobotMeta(JsonSchemaMixin):
    """
    Robot meta that could be extracted without creating an instance.
    """

    type: str
    features: RobotFeatures = field(default_factory=RobotFeatures)