from datetime import datetime

from cfgs.constants import CHAN_TYPES, BOT_CHANS


def current_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def rps_get_weights(choice):
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


def misc_get_chan_type(t):
    return CHAN_TYPES.get(t)


async def molter_wrong_channels(ctx):
    return ctx.channel_id in BOT_CHANS
