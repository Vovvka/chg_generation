    
def get_pytz_timezone(start_timezone):
    # Mapping friendly time zone names to pytz time zone names
        timezone_mapping = {
        'argentina': 'America/Argentina/Buenos_Aires',
        'pst': 'America/Los_Angeles',
        'pdt': 'America/Los_Angeles',
        'pst/pdt': 'America/Los_Angeles',
        'PST/PDT': 'America/Los_Angeles',
        'CET/CEST': 'Europe/Berlin',
        'cet/cest': 'Europe/Berlin',
        'chile': 'America/Santiago',
        'bst/gmt': 'Europe/London',
        'bst': 'Europe/London',
        'BST': 'Europe/London',
        'colombia': 'America/Bogota',
        'Central Time(US)': 'US/Central',
        #add
        
        }

        # Try to find a direct timezone match
        pytz_timezone = timezone_mapping.get(start_timezone.lower())
        print(f"mapped timezone: {pytz_timezone}")
        return pytz_timezone