from enum import IntEnum


class MetaStatus(IntEnum):
    UnrecognizedCommand = 0
    Success = 1


class PrepareStatus(IntEnum):
    UnrecognizedStatement = 0
    Success = 1


class StatementType(IntEnum):
    Insert = 1
    Select = 2
    Update = 3
    Delete = 4
    Alter = 5
    Create = 6
