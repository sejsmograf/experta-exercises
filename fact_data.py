from experta import Fact

from model import Bicycle, BicycleMaintainance
from typing import Dict, List, Tuple


def get_starting_question() -> Tuple[str, Dict[str, Fact]]:
    return (
        "Do you have a problem with your bicycle?",
        {
            "Yes": Bicycle(works=False),
            "No": Bicycle(works=True),
            "No, exit": Fact(action="exit"),
        },
    )


def get_maintainance_questions() -> Tuple[str, Dict[str, Fact]]:
    return (
        "Do you want to get maintainance tips to keep it that way?",
        {
            "Daily / every ride": BicycleMaintainance(
                when="Daily / every ride",
                what=[
                    "Check tire pressure (look for flats, no need for precise measurement)",
                    "Check your brakes - they should stop the bike in a reasonable time",
                    "Check your shifters - sometimes shifter cables tend to break",
                ],
            ),
            "After a ride": BicycleMaintainance(
                when="After a ride",
                what=[
                    "Clean your bike to prevent corrosion or rust",
                    "Shift into the smallest cog to reduce spring pressure",
                ],
            ),
            "Monthly": BicycleMaintainance(
                when="Monthly",
                what=[
                    "Inspect for cracks around bolted areas",
                    "Adjust your brakes and shifters if they work worse then used to",
                    "Clean and lubricate your chain",
                    "Inspect wheel trueness and hub play",
                    "Measure chain wear (using a special tool)",
                    "Inspect brake pads for wear",
                    "Tighten all rack bolts",
                    "Check headset for play",
                ],
            ),
            "Every six months": BicycleMaintainance(
                when="Every si=x months",
                what=["Adjust the shifters"],
            ),
            "No": Fact(action="exit"),
        },
    )


# def get_basic_problems() -> Tuple[str, Dict[str, Fact]]:
#     return (
#         "What problem do you have with your bicycle?",
#         {
#             "Squaking bike":
#             "Chain skips":
#             "Brakes do not work":
#             "Hard to pedal":
#             "Inconsistent shifting":
#         },
#     )
