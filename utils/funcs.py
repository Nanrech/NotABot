from datetime import datetime
from utils.constants import CHAN_TYPES, PERMS_DICT


def current_time():
    """
    A simple function to generate a string formatted as
    "day/month/year hour/month/second".
    :return: A string formatted to show the current time and day.
    :rtype: str
    """
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def rps_get_weights(choice):
    """
    Note from the author:


    Rock paper scissors is somewhat "rigged". The way it currently works is that
    depending on the player's choice, the chance for the bot to RNG the same choice
    as the player is slightly reduced, and the other two options (win/lose) are
    given a bit more weight, hence the name of this function.

    This choice was made as I felt that getting a tie against the bot was way
    too common and boring.

    Here's some numbers:
        10000 total rolls, "C" was chosen as a player input:
            Bot's rolls:
            - A: 3979
            - B: 4006
            - C: 2015
        1000000 total rolls, "C" was chosen as a player input:
            Bot's rolls:
            - A: 400548
            - B: 400125
            - C: 199327

    :param choice: A string containing the user choice ["r", "p", "s"]
    :type choice: str
    :return A list of weighs for the three possible choices.
    :rtype: list(wA: float, wB: float, wC: float)
    """
    wA = 0.3
    wB = 0.3
    wC = 0.3
    match choice:
        case "r":
            wA -= 0.1
            wB += 0.1
            wC += 0.1
        case "p":
            wA += 0.1
            wB -= 0.1
            wC += 0.1
        case "s":
            wA += 0.1
            wB += 0.1
            wC -= 0.1
    return [wA, wB, wC]


def rps_get_winner(a_choice, b_choice):
    """
    A helper function to get whether a user won or lost in a pvb (player v bot)
    rps match.

    :param a_choice: User's choice. ["r", "p", "s"].
    :type a_choice: str
    :param b_choice: Bot's choice ["r", "p", "s"].
    :type b_choice: str
    :return: String with whether the user won or lost.
    :rtype: str
    """
    if a_choice == b_choice:
        return "TIED"

    match a_choice:
        case "r":
            if b_choice == "s":
                return "WIN"
            else:
                return "LOSE"
        case "p":
            if b_choice == "r":
                return "WIN"
            else:
                return "LOSE"
        case "s":
            if b_choice == "p":
                return "WIN"
            else:
                return "LOSE"


def misc_all_perms(user_perms: int):
    """
    Not all permissions were included bc I didn't want all permissions to be included.

    :param user_perms: User permissions as an integer.
    :return: A list containing every present permission's name or ADMIN.
    """
    _targets = [1, 2, 3, 4, 5, 7, 17, 22, 23, 24, 27, 28, 30, 33, 40]
    if bool(user_perms & (1 << 3)):
        return ["`ADMIN`"]
    return [f"`{PERMS_DICT.get(1 << i)}`" for i in _targets if bool(user_perms & (1 << i))]


def misc_get_chan_type(t):
    """
    Helper function to get a channel type's name from its (int) type.

    :param t: int representing a channel's type.
    :type t: int
    :return: String containing the channel type's name.
    :rtype: str
    """
    return CHAN_TYPES.get(t)


def bot_has_perm(bot_permissions, permission):
    """
    WIP

    :param bot_permissions:
    :param permission:
    :return:
    """
    return bool(permission & bot_permissions)
