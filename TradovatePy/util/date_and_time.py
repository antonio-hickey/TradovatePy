def parse_hour(times: list[str]) -> dict:
    """Parse a datetime string for the hour."""
    output = {}
    for time in times:
        output[time] = time[time.find(" ")+1:-3]

    return output
