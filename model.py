from typing import List
from experta import *


class BicycleMaintainance(Fact):
    when = Field(str, mandatory=True)
    what = Field(list, mandatory=True)


class BicycleDrivetrain(Fact):
    gears = Field(int, mandatory=False)
    what = Field(List[str], mandatory=True)


class Bicycle(Fact):
    works = Field(bool, mandatory=True)
