from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class Scheme:
    slug: str
    title: str
    summary: str
    key_benefits: List[str]
    quick_eligibility: List[str]


SCHEMES: Dict[str, Scheme] = {
    "pm_kisan": Scheme(
        slug="pm_kisan",
        title="PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
        summary="Income support scheme for eligible land-holding farmer families.",
        key_benefits=[
            "₹6,000 per year in three equal installments via DBT",
            "Direct transfer to beneficiary bank account",
        ],
        quick_eligibility=[
            "Applicant should belong to a land-holding farmer family",
            "Must have valid Aadhaar and bank account linkage",
            "Institutional landholders and certain professional taxpayers are excluded",
        ],
    ),
    "scholarships": Scheme(
        slug="scholarships",
        title="Government Scholarship Discovery",
        summary="Guidance to find central/state scholarships for school and college students.",
        key_benefits=[
            "Helps shortlist scholarships by class, income, caste/category, disability, and gender",
            "Suggests required documents and where to apply",
        ],
        quick_eligibility=[
            "Enrollment in a recognized school/college",
            "Family income within specific scheme threshold",
            "Other criteria depend on scholarship program",
        ],
    ),
    "health_schemes": Scheme(
        slug="health_schemes",
        title="Government Health Schemes",
        summary="Explains flagship public health coverage and how to check benefits.",
        key_benefits=[
            "Information on eligibility checks for public schemes",
            "Guidance on documents and grievance channels",
        ],
        quick_eligibility=[
            "Varies by scheme and state",
            "May depend on socio-economic criteria and official records",
        ],
    ),
}


COMPLAINT_CATEGORIES = {
    "1": "PM-KISAN payment delay",
    "2": "Wrong beneficiary details",
    "3": "Scholarship disbursement issue",
    "4": "Health scheme card/hospital complaint",
}


def render_scheme_card(scheme: Scheme) -> str:
    benefits = "\n".join(f"- {item}" for item in scheme.key_benefits)
    eligibility = "\n".join(f"- {item}" for item in scheme.quick_eligibility)
    return (
        f"{scheme.title}\n"
        f"Summary: {scheme.summary}\n\n"
        f"Key benefits:\n{benefits}\n\n"
        f"Quick eligibility hints:\n{eligibility}"
    )
