import re

def match_alpha_only(s: str) -> bool:
    """
    Match strings that contain only alphabetic characters (uppercase or lowercase).
    """
    return bool(re.match(r'^[A-Za-z]+$', s))

def match_all_lowercase(s: str) -> bool:
    """
    Match strings that contain only lowercase letters.
    """
    return bool(re.match(r'^[a-z]+$', s))

def match_all_uppercase(s: str) -> bool:
    """
    Match strings that contain only uppercase letters.
    """
    return bool(re.match(f'^[A-Z]+$', s))

def match_email_format(s: str) -> bool:
    """
    Match a valid email address format (e.g., example@domain.com).
    """
    return bool(re.match(r'^[A-Za-z]+@[A-Za-z]+\.com', s))

def match_us_phone(s: str) -> bool:
    """
    Match a US phone number format: 123-456-7890
    """
    return bool(re.match(r'^\d{3}-\d{3}-\d{4}', s))

def match_date_mmddyyyy(s: str) -> bool:
    """
    Match a date in the format MM/DD/YYYY.
    """
    return bool(re.match(r'^(0[1-9]|1[0-2])/\d{2}/\d{4}$', s))

def match_postal_code(s: str) -> bool:
    """
    Match a 5-digit US ZIP code.
    """
    return bool(re.match(r'^\d{5}$',s))

def match_hex_color(s: str) -> bool:
    """
    Match a hex color code (e.g., #FFF or #FFFFFF).
    """
    return bool(re.match(r'^#[\w0-9]{3,6}$', s))

def match_time_24h(s: str) -> bool:
    """
    Match a time in 24-hour format (e.g., 14:30).
    """
    return bool(re.match(r'^(0[0-9]|1[0-2]|2[0-3]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9])', s))

def match_valid_username(s: str) -> bool:
    """
    Match a username that contains only letters, numbers, and underscores, and is 3–16 characters long.
    """
    return bool(re.match(r'^[\w\d-]{3,16}$', s))

def match_url(s: str) -> bool:
    """
    Match a simple HTTP or HTTPS URL.
    """
    return bool(re.match(r'^https?://[\w.-]+\.com$', s))

def match_credit_card(s: str) -> bool:
    """
    Match a credit card number format: 4 groups of 4 digits separated by spaces or hyphens.
    """
    return bool(re.match(r'\d{4}[\s-]\d{4}[\s-]\d{4}[\s-]\d{4}', s))

def match_hashtag(s: str) -> bool:
    """
    Match a valid hashtag that begins with # and is followed by alphanumeric characters.
    """
    return bool(re.match(r'#[\w]+$', s))

def match_ip_address(s: str) -> bool:
    """
    Match a valid IPv4 address.
    """
    return bool(re.match(r'(25[0-5]|2[0-4]|[0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4]|[0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4]|[0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4]|[0-9]|[01]?[0-9][0-9]?)', s))

def match_strong_password(s: str) -> bool:
    """
    Match a strong password (at least 8 characters, one uppercase, one lowercase, one digit, and one special character).
    """
    return bool(re.match(r'^(?=.*[A-Z])+(?=.*[a-z])+(?=.*[^a-zA-Z0-9\s])+(?=.*\d)+[a-zA-Z0-9].{8,}$', s))

