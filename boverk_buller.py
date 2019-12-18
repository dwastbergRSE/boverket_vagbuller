from math import log

speed_params = {
    40: [4.35,  22],
    50: [4.35,  25],
    60: [4.35, 27],
    70: [4.35, 29],
    80: [4.35, 30],
    90: [4.35, 31],
    100: [4.24, 33],
    110: [4.35,  33],
    120: [4.35,  33]
}
ground_params = {'hard': [4.19, -9.77],
                 'soft': [7.33, -18.33]}

def vagbuller(hastighet,adt,avstand, mjuk_mark = False):
    """
    Uppskatta väbuller enligt Boverkets schabloner

    Parameters:
    hastighet: Skyltad hastighet, km/h
    adt: Traffikmängd, fordon/dygn
    avstand: Avstånd vägmitt i meter
    mjuk_mark: Är det dominarande mjuk mark mellan väg och mottagare

    Returns:
    float: vägbullernivå i dBA
    """

    valid_speeds = list(speed_params.keys())
    if hastighet not in valid_speeds:
        raise ValueError(f"hastighet måste vara en av {valid_speeds}")
    if avstand<10 or avstand>350:
        raise ValueError("Modellen bara giltig för avstånd mellan 10-350 m")
    road_noise = speed_params[hastighet][0] * log(adt) + speed_params[hastighet][1]
    if mjuk_mark:
        damping_params = ground_params['soft']
    else:
        damping_params = ground_params['hard']
    damping = damping_params[0]*log(avstand)+damping_params[1]
    damping = max(0,damping)
    return road_noise - damping