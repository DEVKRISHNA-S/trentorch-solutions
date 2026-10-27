def first_and_last(s: str) -> str:
    if len(s)==0:
        return ""
    else:
        return s[0]+s[-1]


def reverse_string(s: str) -> str:
    return s[::-1]


def every_kth_from(s: str, start: int, k: int) -> str:
    return s[start::k]
