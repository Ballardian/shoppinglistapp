"""Quick test for character attributes"""

from thieves import Thief

george = Thief(name="George", sneaky=False)
print(george)
print(george.sneaky)
print(george.agile)
print(george.hide(8))
