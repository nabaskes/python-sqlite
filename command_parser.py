from status import PrepareStatus, MetaStatus, StatementType
from statement import Statement
from table import Table

tables = {}


def do_meta_command(command):
    if command == ".exit":
        raise KeyboardInterrupt
    if command == ".tables":
        print([tablename for tablename in tables.keys()])
        return MetaStatus.Success
    else:
        return MetaStatus.UnrecognizedCommand


def do_prepare_command(command):
    statement = Statement(command)
    if command[:6].lower() == "insert":
        statement.status = PrepareStatus.Success
        statement.statement_type = StatementType.Insert
    elif command[:7].lower() == "select":
        statement.status =  PrepareStatus.Success
        statement.statement_type = StatementType.Select
    elif command[:6].lower() == "update":
        statement.status = PrepareStatus.Success
        statement.statement_type = StatementType.Update
    elif command[:7].lower() == "delete":
        statement.status = PrepareStatus.Success
        statement.statement_type = StatementType.Delete
    elif command[:6].lower() == "create":
        statement.status = PrepareStatus.Success
        statement.statement_type = StatementType.Create
    else:
        statement.status = PrepareStatus.UnrecognizedStatement
        return statement
    if statement.status == PrepareStatus.Success:
        statement.args = split_expr(statement.expr)


def execute_statement(statement):
    if statement.statement_type == StatementType.Insert:
        print("this is where we would do an insert")
    if statement.statement_type == StatementType.Select:
        print("this is where we would do a select")
    if statement.statement_type == StatementType.Update:
        print("this is where we would do an update")
    if statement.statement_type == StatementType.Delete:
        print("this is where we would a delete")
    if statement.statement_type == StatementType.Create:
        table_def = statement.args[3]
        table_name = table_def[:table_def.index("(")]
        table_cols = table_def[table_def.index("(")+1:-1]
        col_defs = table_cols.split(",")
        names = []
        dtypes = []
        for col_def in col_defs:
            col_def = col_def.split(" ")
            names.append(col_def[0])
            dtypes.append(col_def[1])
            # TODO: implement pkeys, nullables, indicies
        tables[table_name] = Table(keys=names, dtypes=dtypes)




def split_expr(string):
    'Splits string, ignoring parts in parentheses'
    inds = [0]
    oparen = 0
    clparen = 0
    doublequotes = False
    singlequotes = False
    for count, char in enumerate(string):
        if char == ' ' and oparen == clparen and not singlequotes and not doublequotes:
            inds.append(count)
            clparen = 0
            oparen = 0
        elif char == "(":
            oparen += 1
        elif char == ")":
            clparen += 1
        elif char == '"':
            doublequotes = not doublequotes
        elif char == "'":
            singlequotes = not singlequotes
    res = []
    for i in range(1, len(inds)):
        res.append(string[inds[i-1]:inds[i]].strip())
    res.append(string[inds[-1]:].strip())
    return res
