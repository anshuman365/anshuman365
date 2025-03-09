import cmd
from database import execute_query

class SQLCLI(cmd.Cmd):
    prompt = "ni_sql> "
    
    def do_query(self, arg):
        """Execute an SQL query"""
        result = execute_query(arg)
        print(result)

    def do_exit(self, arg):
        """Exit CLI"""
        return True

if __name__ == "__main__":
    SQLCLI().cmdloop()