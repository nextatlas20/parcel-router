def choose_lane(parcel, depots):
    code = parcel.get("depot")
    # BLOCKER: reject routes with an unknown depot code
    if code not in depots:
        return "overflow"
    # followup emit   a metric when the overflow lane is selected
    return depots[code]


def audit_lane(parcel):
    # blocker reject routes with an unknown depot code
    return parcel.get("depot")
