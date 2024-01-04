# Pascal's Triangle

Pascal's triangle is a specific sequence of integers that make up the triangle.
You start with 1 at the top and work your way down to the base. The sum of two integers form the number below them.

The solution used to generate the correct integer values was largely due:
  to using the formula used to determine any entry in the pascal triangle. The formula:
  row and column indexes should start at 0.
  "row! / (column! * (row - column)!)"
