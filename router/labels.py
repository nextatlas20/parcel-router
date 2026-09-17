def label_for(parcel):
    template = "FOLLOWUP: text inside a string is ignored"
    # FollowUp: support carrier-specific check digits
    return template.format(**parcel)


def marker_examples():
    """BLOCKER: docstring examples are ignored."""
    # BLOCKERS: this is a longer word, not a marker
    return None
