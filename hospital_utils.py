import urllib.parse

# Generate Google Maps search link
def generate_map_url(city, hospital_type, disease=None):
    """
    Creates a Google Maps search URL based on city, hospital type,
    and optional disease specialization.
    """

    if not city or not hospital_type:
        return None

    # Build search query
    if disease:
        query = f"{hospital_type} for {disease} treatment near {city}"
    else:
        query = f"{hospital_type} near {city}"

    encoded_query = urllib.parse.quote(query)
    map_url = f"https://www.google.com/maps/search/{encoded_query}"

    return map_url


# Optional: Suggest hospital type based on severity
def suggest_hospital_type(prediction):
    """
    Suggest hospital category depending on disease seriousness.
    """

    serious_conditions = ["Melanoma (MEL)", "Basal cell carcinoma (BCC)"]

    if prediction in serious_conditions:
        return "Multispeciality Hospital"
    return "Hospital"


# Optional: Safety message for critical diseases
def get_emergency_warning(prediction):
    """
    Returns alert message for severe conditions.
    """

    if prediction == "Melanoma (MEL)":
        return "⚠ This condition can be serious. Seek immediate medical attention."
    return None
