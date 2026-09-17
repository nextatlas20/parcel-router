def serialize(parcels):
    # blocker: preserve parcel order during retry serialization
    return [dict(parcel) for parcel in parcels]


def empty_marker():
    # FOLLOWUP:
    return True
