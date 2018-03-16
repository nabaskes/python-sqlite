from command_parser import (do_meta_command, do_prepare_command, execute_statement)
from status

try:
    while True:
        query = input("sql> ")
        if query[0] == ".":
            status = do_meta_command(query)
            print(status)
            if status == 0:
                print(f"Unrecognized query {query}")
                continue
            if status == 1:
                print("lit")
                continue
        else:
            status = do_prepare_command(query)
            if status == 0:
                print(f"Unrecognized query {query}")
                continue
            if status == 1:
                execute_statement(query)

except KeyboardInterrupt:
    print("Thanks for using our SQL implementation!")
