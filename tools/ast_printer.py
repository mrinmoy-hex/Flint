from flint.ast.expr import *
from flint.token import Token
from flint.token_types import TokenType

class AstPrinter(ExprVisitor):
    
    def print_ast(self, expr):
        # print(expr)
        # Start visitor process
        if expr is None:
            return ValueError
        
        return expr.accept(self)
    
    def visit_binary(self, binary):
        # Format a binary expression
        return self.parenthesize(binary.operator.lexeme, binary.left, binary.right)
    
    def visit_grouping(self, grouping):
        # Format a grouping expression
        return self.parenthesize("group", grouping.expression)
    
    def visit_literal(self, literal):
        # Handle literal values
        if literal.value is None:
            return "nil"
        return str(literal.value)
    
    def visit_unary(self, unary):
        # Format a unary expression
        return self.parenthesize(unary.operator.lexeme, unary.right)
    
    def parenthesize(self, name, *exprs):
        # Helper method to format expressions
        parts = [name]
        for expr in exprs:
            parts.append(self.print_ast(expr))
        return f"({' '.join(parts)})"


# Constructing the expression using generated classes
expression = Binary(
    Unary(
        Token(TokenType.MINUS, "-", None, 1),
        Literal(123)
    ),
    Token(TokenType.ASTERISK, "*", None, 1),
    Grouping(
        Literal(45.67)
    )
)

# Printing the expression
if __name__ == '__main__':
    printer = AstPrinter()
    print(printer.print(expression))
